from phi.agent import Agent
from phi.model.groq import Groq
from phi.tools.yfinance import YFinanceTools
from phi.tools.duckduckgo import DuckDuckGo
from dotenv import load_dotenv
import os
import phi.api
import openai
# Load environment variables from .env file
load_dotenv()
openai.api_key = os.getenv("OPENAI_API_KEY")
Groq_API_KEY = os.getenv("GROQ_API_KEY")
phi.api_key = os.getenv("PHI_API_KEY")
## Web Search Agent
web_search_agent = Agent(
    name = "Web Search Agent",
    role = "Search the web for the information",
    model = Groq(id="llama3-70b-8192"),
    tools = [DuckDuckGo()],
    instructions= ["Always include the sources"],
    show_tool_calls=True,
    markdown=True,
    
)

## Financial Agent

finance_agent = Agent(
    name = "Financial Agent",
    model = Groq(id="llama3-70b-8192"),
    tools = [
        YFinanceTools(stock_price=True, analyst_recommendations=True, stock_fundamentals=True,
                      company_news= True),
    ],
    instructions = ["Use Tables to Display the Data"],
    show_tool_calls=True, #show all tool calls made by the agent
    markdown=True, # formatng the output in markdown for better readability
)

# IF COMBINE BOTH AGENTS IT BOCOME MULTI AGENT

multi_ai_agent = Agent(
    team = [web_search_agent, finance_agent],
    instructions = ["Always include the sources", "Use Tables to Display the Data"],
    show_tool_calls= True,
    markdown=True,
)   

multi_ai_agent.print_response("Summarize analyst recommendation and share the latest news for Tesla", stream=False)

