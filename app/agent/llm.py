from langchain_groq import ChatGroq
from app.core.config import settings

def get_groq_llm() -> ChatGroq:
    """Initializes and returns the ChatGroq model instance."""
    return ChatGroq(
        groq_api_key=settings.GROQ_API_KEY,
        model_name=settings.GROQ_MODEL,
        temperature=0.2
    )