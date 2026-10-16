import pandas as pd
from typing import Dict, Any
from app.services.dataset_service import DatasetService

class AnalyticsService:
    @staticmethod
    def _prepare_revenue(df: pd.DataFrame) -> pd.DataFrame:
        df = df.copy()
        if "revenue" not in df.columns:
            if "quantity" in df.columns and "unit_price" in df.columns:
                df["revenue"] = df["quantity"] * df["unit_price"]
        return df

    @classmethod
    def analyze_sales(cls, dataset_id: str, metric: str = "total") -> Dict[str, Any]:
        df = DatasetService.get_dataframe(dataset_id)
        df = cls._prepare_revenue(df)

        if "revenue" not in df.columns:
            return {"error": "Revenue calculation failed. Dataset lacks 'revenue' or ('quantity', 'unit_price')."}

        total_revenue = float(df["revenue"].sum())
        rows_considered = len(df)

        result = {
            "total_revenue": round(total_revenue, 2),
            "rows_considered": rows_considered,
            "revenue_derived": "revenue" not in df.columns
        }

        if "product" in df.columns:
            prod_rev = df.groupby("product")["revenue"].sum().reset_index()
            top_prod = prod_rev.sort_values(by="revenue", ascending=False).iloc[0]
            result["top_product"] = top_prod["product"]
            result["top_product_revenue"] = round(float(top_prod["revenue"]), 2)
            
            top_5 = prod_rev.sort_values(by="revenue", ascending=False).head(5)
            result["top_5_products"] = top_5.to_dict(orient="records")

        if "order_id" in df.columns:
            avg_order_val = df.groupby("order_id")["revenue"].sum().mean()
            result["average_order_value"] = round(float(avg_order_val), 2)

        return result

    @classmethod
    def analyze_customers(cls, dataset_id: str) -> Dict[str, Any]:
        df = DatasetService.get_dataframe(dataset_id)
        
        if "segment" not in df.columns:
            return {"error": "Missing 'segment' column for customer analysis."}

        segment_counts = df["segment"].value_counts().to_dict()
        res = {"segment_counts": segment_counts}

        churn_col = [c for c in df.columns if c in ["churned", "churn", "is_churned"]]
        if churn_col:
            c_name = churn_col[0]
            churn_rates = df.groupby("segment")[c_name].apply(lambda x: (x.astype(bool)).mean() * 100).to_dict()
            res["churn_rates_pct"] = {k: round(v, 2) for k, v in churn_rates.items()}
        else:
            res["churn_note"] = "Churn analysis unavailable: No explicit churn field present."

        return res

    @classmethod
    def analyze_trends(cls, dataset_id: str) -> Dict[str, Any]:
        df = DatasetService.get_dataframe(dataset_id)
        df = cls._prepare_revenue(df)

        date_col = [c for c in df.columns if "date" in c or "time" in c]
        if not date_col:
            return {"error": "No date column found for monthly trend analysis."}

        d_name = date_col[0]
        df[d_name] = pd.to_datetime(df[d_name], errors="coerce")
        df = df.dropna(subset=[d_name])

        df["year_month"] = df[d_name].dt.to_period("M").astype(str)
        monthly = df.groupby("year_month")["revenue"].sum().reset_index()
        monthly["prev_revenue"] = monthly["revenue"].shift(1)
        monthly["change"] = monthly["revenue"] - monthly["prev_revenue"]
        monthly["pct_change"] = (monthly["change"] / monthly["prev_revenue"]) * 100

        max_drop = monthly.sort_values(by="change", ascending=True).iloc[0] if len(monthly) > 1 else None

        return {
            "monthly_series": monthly.to_dict(orient="records"),
            "largest_decrease": {
                "month": max_drop["year_month"] if max_drop is not None else None,
                "revenue": round(float(max_drop["revenue"]), 2) if max_drop is not None else None,
                "decrease_amount": round(float(abs(max_drop["change"])), 2) if max_drop is not None else None,
                "pct_decrease": round(float(abs(max_drop["pct_change"])), 2) if max_drop is not None else None
            } if max_drop is not None else "Insufficient period data for mom changes."
        }