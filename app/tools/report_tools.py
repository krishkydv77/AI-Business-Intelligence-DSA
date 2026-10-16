from langchain.tools import tool
from app.services.report_service import ReportService

@tool
def report_generation_tool(dataset_id: str, report_type: str = "sales_overview") -> str:
    """Builds a full structured executive report with KPIs, findings, and recommendations."""
    res = ReportService.build_executive_report(dataset_id, report_type)
    return str(res)