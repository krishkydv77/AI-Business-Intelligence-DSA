# AI Business Intelligence & Decision Support Agent

**An AI-powered business analytics platform that transforms CSV datasets into evidence-based business insights using LangChain, Groq, FastAPI, and Pandas.**

## Overview

The AI Business Intelligence & Decision Support Agent enables users to upload business datasets and ask questions in natural language. A LangChain tool-calling agent selects the appropriate analytical tools, Pandas performs deterministic calculations, and Groq-powered LLM responses explain the results in clear business language.

The platform supports sales and revenue analysis, product performance ranking, monthly trend analysis, customer segmentation, conditional churn analysis, dataset profiling, and executive report generation through REST APIs.

## Key Features

- **CSV Data Ingestion:** Upload business datasets with validation and dataset ID registration.
- **Dataset Profiling:** Inspect row counts, columns, data types, missing values, and available date ranges.
- **AI-Powered Question Answering:** Ask business questions in natural language.
- **Tool-Calling Agent:** Uses LangChain to select relevant analytical tools.
- **Sales & Revenue Analytics:** Calculate total revenue, product-wise revenue, top-performing products, and average order value.
- **Trend Analysis:** Compare monthly sales, calculate absolute and percentage changes, and identify declining periods.
- **Customer Analytics:** Analyze customer segments and churn rates when valid churn data is available.
- **Evidence-Based Insights:** Return calculated values, supporting evidence, filters, and relevant caveats.
- **Executive Reporting:** Generate structured business summaries, KPIs, findings, and data-quality warnings.
- **REST API:** Access functionality through FastAPI endpoints and interactive Swagger documentation.
- **Validation & Error Handling:** Handle invalid files, missing datasets, unsupported questions, and missing analytical columns.
- **Automated Testing:** Verify API behavior and analytical calculations.

## Technology Stack

| Category | Technologies |
|---|---|
| Language | Python |
| API Framework | FastAPI, Uvicorn |
| AI Agent Framework | LangChain |
| LLM Provider | Groq |
| Data Processing | Pandas, NumPy |
| Data Validation | Pydantic |
| Configuration | Python-dotenv |
| Testing | Pytest, FastAPI TestClient |
| Data Storage | Local CSV storage; SQLite if configured |

## Architecture

```text
             User / API Client
                     |
                     v
             FastAPI Application
                     |
          +----------+----------+
          |                     |
          v                     v
    CSV Data Upload       Business Query
          |                     |
          v                     v
    Dataset Service       LangChain Agent
          |                     |
          v                     v
    CSV Validation        Tool Selection
          |                     |
          |          +----------+----------+
          |          |          |          |
          |          v          v          v
          |        Sales      Trends    Customers
          |          |          |          |
          +----------+----------+----------+
                                |
                                v
                       Pandas Analytics
                                |
                                v
                      Calculated Evidence
                                |
                                v
                       Groq-Powered LLM
                                |
                                v
                   Business Insights / Report
```

**Core principle:** The LLM selects analytical capabilities and explains their results. Pandas performs the actual business calculations, keeping numerical results separate from AI-generated text.

## Installation and Setup

### 1. Clone the repository

```bash
git clone https://github.com/YOUR_USERNAME/AI-Business-Intelligence-DSA.git
cd AI-Business-Intelligence-DSA
```

Replace `YOUR_USERNAME` with your GitHub username.

### 2. Create a virtual environment

For Windows PowerShell:

```powershell
python -m venv .venv
.\.venv\Scripts\Activate.ps1
```

### 3. Install dependencies

```bash
python -m pip install --upgrade pip
pip install -r requirements.txt
```

### 4. Configure environment variables

Create a `.env` file in the project root based on `.env.example`.

```env
GROQ_API_KEY=your_groq_api_key
GROQ_MODEL=your_supported_groq_model
```

Use the model name supported by your Groq account and the model configured in your application.

### 5. Run the application

```bash
uvicorn app.main:app --reload
```

The server will start at:

- API base URL: `http://127.0.0.1:8000`
- Swagger UI: `http://127.0.0.1:8000/docs`
- ReDoc: `http://127.0.0.1:8000/redoc`

## API Endpoints

| Method | Endpoint | Purpose |
|---|---|---|
| GET | `/health` | Check service status |
| POST | `/data/upload` | Upload and register a CSV dataset |
| GET | `/data/{dataset_id}/profile` | Retrieve dataset profile and quality information |
| POST | `/business/query` | Ask a natural-language business question |
| POST | `/business/report` | Generate an executive report |

## How the AI Agent Works

1. The user uploads a CSV dataset.
2. The dataset service validates and registers the dataset.
3. The user submits a business question with the dataset ID.
4. The LangChain agent identifies the appropriate analytical capability.
5. The selected tool invokes deterministic Pandas-based calculations.
6. The analytical result is returned as structured evidence.
7. Groq generates a business-friendly explanation grounded in the computed result.
8. FastAPI returns a structured response to the client.

The model is not given arbitrary Python execution or unrestricted access to the server. Analytical tools should validate their inputs and return only the information required for the requested task.


*Built to make business data easier to query, analyze, and turn into evidence-based decisions.*
