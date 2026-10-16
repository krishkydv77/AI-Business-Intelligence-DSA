from fastapi import FastAPI
from app.schemas.response_models import HealthResponse
from app.api.routes import data_routes, business_routes

app = FastAPI(
    title="AI Business Intelligence & Decision Support Agent",
    description="Backend API powered by FastAPI, LangChain Agent, Groq LLM, and Pandas",
    version="1.0.0"
)

app.include_router(data_routes.router)
app.include_router(business_routes.router)

@app.get("/health", response_model=HealthResponse, tags=["Health"])
async def health_check():
    return HealthResponse(status="healthy", version="1.0.0")