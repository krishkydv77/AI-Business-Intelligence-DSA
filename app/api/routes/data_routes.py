from fastapi import APIRouter, UploadFile, File
from app.schemas.response_models import UploadResponse, ProfileResponse
from app.services.dataset_service import DatasetService
from app.services.analytics_service import AnalyticsService

router = APIRouter(prefix="/data", tags=["Data Processing"])

@router.post("/upload", response_model=UploadResponse)
async def upload_csv(file: UploadFile = File(...)):
    contents = await file.read()
    res = DatasetService.save_and_validate(contents, file.filename)
    return UploadResponse(success=True, **res)

@router.get("/{dataset_id}/profile", response_model=ProfileResponse)
async def get_profile(dataset_id: str):
    df = DatasetService.get_dataframe(dataset_id)
    
    date_cols = [c for c in df.columns if "date" in c or "time" in c]
    date_range = None
    if date_cols:
        d = df[date_cols[0]].dropna()
        if not d.empty:
            date_range = {"min": str(d.min()), "max": str(d.max())}

    return ProfileResponse(
        dataset_id=dataset_id,
        row_count=len(df),
        column_types={col: str(dtype) for col, dtype in df.dtypes.items()},
        missing_values=df.isnull().sum().to_dict(),
        date_range=date_range,
        available_metrics=["sales", "revenue", "trends", "customer_segment"]
    )