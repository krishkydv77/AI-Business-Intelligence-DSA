from langchain.tools import tool
from app.services.analytics_service import AnalyticsService

@tool
def trend_analysis_tool(dataset_id: str) -> str:
    """Calculates monthly sales trends, period-over-period changes, and largest drops."""
    res = AnalyticsService.analyze_trends(dataset_id)
    return str(res)