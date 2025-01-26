from phi.agent import Agent
from phi.model.groq import Groq
from phi.tools.yfinance import YFinanceTools
from phi.tools.duckduckgo import DuckDuckGo


import os
from dotenv import load_dotenv
load_dotenv()

## web search agent
web_search_agent=Agent(
    name="Web Search Agent",
    role="Search the website for the given input text and give information in few sentences ",
    model=Groq(id="llama-3.3-70b-versatile", api_key=os.environ.get("GROQ_API_KEY")),
    tools=[DuckDuckGo()],
    instructions=["Alway include sources"],
    show_tools_calls=True,
    markdown=True,

)

## Financial agent
finance_agent=Agent(
    name="Finance AI Agent",
    model=Groq(id="llama-3.3-70b-versatile",api_key=os.environ.get("GROQ_API_KEY")),
    tools=[
        YFinanceTools(stock_price=True, analyst_recommendations=True, stock_fundamentals=True,
                      company_news=True),
    ],
    instructions=["give information regarding input text in few sentences"],
    show_tool_calls=True,
    markdown=True,

)

stock_agent=Agent(
    name="stock_agent",
    team=[web_search_agent,finance_agent],
    model=Groq(id="llama-3.3-70b-versatile",api_key=os.environ.get("GROQ_API_KEY")),
    instructions=["provide information in few sentences regarding input text "],
    show_tool_calls=True,
    markdown=True,
)

stock_agent.print_response('nvda stock information')

 
