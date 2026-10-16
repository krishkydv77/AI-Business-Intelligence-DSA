from langchain_classic.agents import create_tool_calling_agent, AgentExecutor
from langchain_core.prompts import ChatPromptTemplate, MessagesPlaceholder
from app.agent.llm import get_groq_llm
from app.agent.prompts import SYSTEM_PROMPT
from app.tools.sales_tools import sales_analysis_tool
from app.tools.customer_tools import customer_segment_tool
from app.tools.trend_tools import trend_analysis_tool
from app.tools.report_tools import report_generation_tool

def get_agent_executor():
    llm = get_groq_llm()
    tools = [sales_analysis_tool, customer_segment_tool, trend_analysis_tool, report_generation_tool]

    prompt = ChatPromptTemplate.from_messages([
        ("system", SYSTEM_PROMPT),
        ("human", "{input}"),
        MessagesPlaceholder(variable_name="agent_scratchpad"),
    ])

    agent = create_tool_calling_agent(llm, tools, prompt)
    return AgentExecutor(agent=agent, tools=tools, verbose=True)