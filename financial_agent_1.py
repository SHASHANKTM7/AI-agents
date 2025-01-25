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

# input_query = None  # Define a global variable
# op_response = None
# def save_argument(arg):
#     global input_query  # Use the global variable
#     saved_args = arg
#     print(f"Argument '{arg}' saved.")

# save_argument("Hello, World!")
# print(f"Saved argument: {saved_args}")

# def stock(query):
#     global input_query  # Use the global variable
#     input_query = query
#     global op_response  
#     op_response=stock_agent.print_response(input_query,stream=True)
#     return op_response
stock_agent.print_response('nvda stock information')
# result=stock('short information of NVDA stock')
# print(result)

# checking_agent=Agent(
#     name="checking_agent",
#     model=Groq(id="llama-3.3-70b-versatile",api_key=os.environ.get("GROQ_API_KEY")),
#     instructions=[f" for given context  = {op_response}. and the given query= {input_query}. give iformation about improvements that needs to be made by context regarding query",
#                   "give rankng between 1 to 10 based on performance of context for input query"],
#     show_tool_calls=True,
#     markdown=True,
# )

# checking_agent.print_response()



# feedback_agent= Agent(
#     name="feedback_agent",
#     team=[stock_agent],
#     model=Groq(id="llama-3.3-70b-versatile",api_key=os.environ.get("GROQ_API_KEY")),
#     instructions=[
#         "go through the information provided by stock_agent ",
#         "give information about the quality of content",
#         "give what more information should be added to improve the response",
#     ],
#     show_tool_calls=True,
#     markdown=True,
# )

# feedback_agent..print_response("provide information about the content",stream=True)