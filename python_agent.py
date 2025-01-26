from phi.agent import Agent
from phi.model.groq import Groq
# from phi.tools.yfinance import YFinanceTools
# from phi.tools.duckduckgo import DuckDuckGo
from phi.agent import Agent
from phi.tools.python import PythonTools

import os
from dotenv import load_dotenv
load_dotenv()

## web search agent
code_agent=Agent(
    name="code_agent",
    model=Groq(id="llama-3.3-70b-versatile", api_key=os.environ.get("GROQ_API_KEY")),
    tools=[PythonTools()], show_tool_calls=True,
    markdown=True,

)

code_agent.print_response("write a python code to check if str(2a6b6a2) is a palindrome and show the result",stream=True)
