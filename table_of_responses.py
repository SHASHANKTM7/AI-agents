from phi.agent import Agent
from phi.model.groq import Groq
from phi.tools.yfinance import YFinanceTools
from phi.tools.duckduckgo import DuckDuckGo
from phi.tools.wikipedia import WikipediaTools
from phi.tools.hackernews import HackerNews




import os
from dotenv import load_dotenv
load_dotenv()

 

## Financial agent
wikipidia_agent=Agent(
    name="wikipedia Agent",
    model=Groq(id="llama-3.3-70b-versatile",api_key=os.environ.get("GROQ_API_KEY")),
    tools=[WikipediaTools()],
    instructions=["please provide the information regarding the input text in few sentences"],
    show_tool_calls=True,
    markdown=True,

)

 ## web search agent
web_search_agent=Agent(
    name="Web Search Agent",
    role="Search the website for the given input text and provide information in few sentences",
    model=Groq(id="llama-3.3-70b-versatile", api_key=os.environ.get("GROQ_API_KEY")),
    tools=[DuckDuckGo()],
    instructions=["Alway include sources"],
    show_tools_calls=True,
    markdown=True,

)


multi_agent=Agent(
    name="multi_agent",
    team=[web_search_agent,wikipidia_agent],
    model=Groq(id="llama-3.3-70b-versatile",api_key=os.environ.get("GROQ_API_KEY")),
    instructions=["create a table where each column has responses of each agent"],
    show_tool_calls=True,
    markdown=True,
)


multi_agent.print_response("give information about football worldcup ")
 