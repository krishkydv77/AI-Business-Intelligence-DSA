from typing import Dict, Any
from app.services.analytics_service import AnalyticsService

class ReportService:
    @staticmethod
    def build_executive_report(dataset_id: str, report_type: str = "sales_overview") -> Dict[str, Any]:
        sales = AnalyticsService.analyze_sales(dataset_id)
        trends = AnalyticsService.analyze_trends(dataset_id)
        customers = AnalyticsService.analyze_customers(dataset_id)

        kpis = {
            "total_revenue": sales.get("total_revenue"),
            "top_product": sales.get("top_product"),
            "top_product_revenue": sales.get("top_product_revenue"),
            "average_order_value": sales.get("average_order_value")
        }

        findings = []
        if "top_product" in sales:
            findings.append(f"Top performing product is {sales['top_product']} generating ${sales['top_product_revenue']}.")
        
        if isinstance(trends.get("largest_decrease"), dict):
            ld = trends["largest_decrease"]
            findings.append(f"Largest sales decrease occurred in {ld['month']} dropping by ${ld['decrease_amount']} ({ld['pct_decrease']}%).")

        limitations = ["Causal explanations for sales trends are unavailable from raw data alone."]
        if "churn_note" in customers:
            limitations.append(customers["churn_note"])

        return {
            "success": True,
            "dataset_id": dataset_id,
            "report_type": report_type,
            "executive_summary": "Automated business intelligence analysis based on deterministic dataset calculations.",
            "kpis": kpis,
            "findings": findings,
            "limitations": limitations,
            "recommendations": [
                "Focus inventory and marketing on top performing products.",
                "Investigate root operational issues behind peak decline months."
            ]
        }