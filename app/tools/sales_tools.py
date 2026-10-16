from langchain.tools import tool
from app.services.analytics_service import AnalyticsService

@tool
def sales_analysis_tool(dataset_id: str, metric: str = "total") -> str:
    """Calculates total revenue, top products, and average order value for a dataset."""
    res = AnalyticsService.analyze_sales(dataset_id, metric)
    return str(res)