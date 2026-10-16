from langchain.tools import tool
from app.services.analytics_service import AnalyticsService

@tool
def customer_segment_tool(dataset_id: str) -> str:
    """Summarizes customer counts and churn rates by segment if churn fields are present."""
    res = AnalyticsService.analyze_customers(dataset_id)
    return str(res)