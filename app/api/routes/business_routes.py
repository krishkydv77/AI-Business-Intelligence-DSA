import json
from fastapi import APIRouter
from app.schemas.request_models import QueryRequest, ReportRequest
from app.schemas.response_models import QueryResponse, ReportResponse
from app.agent.agent_factory import get_agent_executor
from app.services.report_service import ReportService

router = APIRouter(prefix="/business", tags=["Business Intelligence"])

@router.post("/query", response_model=QueryResponse)
async def process_query(req: QueryRequest):
    executor = get_agent_executor()
    
    prompt_input = f"Dataset ID: {req.dataset_id}. Business Question: {req.question}"
    result = executor.invoke({"input": prompt_input})
    
    answer_text = result.get("output", "")
    
    return QueryResponse(
        success=True,
        question=req.question,
        answer=answer_text,
        evidence={"dataset_id": req.dataset_id},
        tools_used=["sales_analysis_tool / trend_tool / customer_tool"],
        caveats=["Figures strictly calculated by Pandas from uploaded CSV."]
    )

@router.post("/report", response_model=ReportResponse)
async def generate_report(req: ReportRequest):
    res = ReportService.build_executive_report(req.dataset_id, req.report_type)
    return ReportResponse(**res)