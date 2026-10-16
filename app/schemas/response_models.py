from pydantic import BaseModel
from typing import List, Dict, Any, Optional

class HealthResponse(BaseModel):
    status: str
    version: str

class UploadResponse(BaseModel):
    success: bool
    dataset_id: str
    filename: str
    row_count: int
    columns: List[str]
    warnings: List[str]

class ProfileResponse(BaseModel):
    dataset_id: str
    row_count: int
    column_types: Dict[str, str]
    missing_values: Dict[str, int]
    date_range: Optional[Dict[str, str]]
    available_metrics: List[str]

class QueryResponse(BaseModel):
    success: bool
    question: str
    answer: str
    evidence: Dict[str, Any]
    tools_used: List[str]
    caveats: List[str]

class ReportResponse(BaseModel):
    success: bool
    dataset_id: str
    report_type: str
    executive_summary: str
    kpis: Dict[str, Any]
    findings: List[str]
    limitations: List[str]
    recommendations: List[str]