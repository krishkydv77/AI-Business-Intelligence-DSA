import uuid
import pandas as pd
from pathlib import Path
from app.core.config import settings
from app.core.exceptions import DatasetNotFoundError, InvalidCSVError

class DatasetService:
    @staticmethod
    def save_and_validate(file_bytes: bytes, filename: str) -> dict:
        dataset_id = f"ds_{uuid.uuid4().hex[:8]}"
        file_path = settings.UPLOAD_DIR / f"{dataset_id}.csv"

        try:
            with open(file_path, "wb") as f:
                f.write(file_bytes)
            
            df = pd.read_csv(file_path)
        except Exception as e:
            if file_path.exists():
                file_path.unlink()
            raise InvalidCSVError(str(e))

        warnings = []
        if df.empty:
            raise InvalidCSVError("Uploaded CSV file is empty.")

        # Normalize column names
        df.columns = df.columns.str.strip().str.lower()
        df.to_csv(file_path, index=False)

        # Revenue logic checks
        if "revenue" not in df.columns:
            if "quantity" in df.columns and "unit_price" in df.columns:
                warnings.append("Revenue column was derived as (quantity * unit_price).")
            else:
                warnings.append("No revenue or (quantity, unit_price) columns found.")

        return {
            "dataset_id": dataset_id,
            "filename": filename,
            "row_count": len(df),
            "columns": list(df.columns),
            "warnings": warnings
        }

    @staticmethod
    def get_dataframe(dataset_id: str) -> pd.DataFrame:
        file_path = settings.UPLOAD_DIR / f"{dataset_id}.csv"
        if not file_path.exists():
            raise DatasetNotFoundError(dataset_id)
        
        df = pd.read_csv(file_path)
        return df