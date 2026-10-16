from pydantic import BaseModel, Field
from typing import Optional

class QueryRequest(BaseModel):
    dataset_id: str = Field(..., description="Unique dataset identifier obtained after upload")
    question: str = Field(..., description="Business question in plain English")

class ReportRequest(BaseModel):
    dataset_id: str = Field(..., description="Unique dataset identifier obtained after upload")
    report_type: Optional[str] = Field("sales_overview", description="Type of executive report")