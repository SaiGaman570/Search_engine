from langchain_core.messages import AnyMessage
from langchain_core.runnables import RunnableConfig
from langgraph.prebuilt.chat_agent_executor import AgentState
from langgraph.prebuilt import create_react_agent
from  dotenv import load_dotenv
import os
load_dotenv()

from langchain_tavily import TavilySearch

search_tool = TavilySearch(max_results=2)
#tools = [tool]

#def multiply(a: int, b:int) -> int:
#    """Multiply two numbers."""
#    return a * b

def my_tool(prompt: str) ->str:
    """use this tool to search real time data"""
    search_result = search_tool.invoke("How is the weather in denton, Texas today?")
    return str(search_result)
    #print(search_result)
    


def prompt(state: AgentState, config: RunnableConfig) -> list[AnyMessage]:  
    user_name = config["configurable"].get("user_name")
    system_msg = f"You are a helpful assistant. Address the user as {user_name}."
    return [{"role": "system", "content": system_msg}] + state["messages"]
model_name = os.getenv("MODEL_NAME")
print(model_name)
agent = create_react_agent(
    model=f"groq:{model_name}",
    tools=[my_tool],
    prompt=prompt
)

#agent.invoke(
#    {"messages": [{"role": "user", "content": "what is the weather in sf"}]},
#    config={"configurable": {"user_name": "John Smith"}}
#)

def get_response(prompt):
    response = agent.invoke(
    {"messages": [{"role": "user", "content": prompt}]},
    config={"configurable": {"user_name":"SaiGaman"}}
    )
    return response["messages"][1].content

res = get_response("Hi")
print("Airesponse",res)


#res = get_response("What is the weather of denton, Texas now?")
#print("Airesponse",res)