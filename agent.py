import os
from typing import Annotated

from dotenv import load_dotenv
from langchain_core.messages import SystemMessage
from langchain_openai import ChatOpenAI
from langgraph.graph import END, START, StateGraph
from langgraph.graph.message import add_messages
from langgraph.prebuilt import ToolNode, tools_condition
from tools import calculate_budget, search_flights, search_hotels
from typing_extensions import TypedDict

load_dotenv()

with open("system_prompt.txt", "r", encoding="utf-8") as f:
    system_prompt = f.read()


class AgentState(TypedDict):
    messages: Annotated[list, add_messages]


tools_list = [search_flights, search_hotels, calculate_budget]
llm = ChatOpenAI(
    model="gpt-4o-mini",
    base_url="https://models.inference.ai.azure.com/",
    api_key=os.getenv("AZURE_OPENAI_API_KEY"),
)
llm_with_tools = llm.bind_tools(tools_list)


def agent_node(state: AgentState):
    messages = state["messages"]
    if not isinstance(messages[0], SystemMessage):
        messages = [SystemMessage(content=system_prompt)] + messages
    response = llm_with_tools.invoke(messages)

    if response.tool_calls:
        for tc in response.tool_calls:
            print(f"Gọi tool: {tc['name']}({tc['args']})")
    else:
        print(f"Trả lời trực tiếp")

    return {"messages": [response]}


builder = StateGraph(AgentState)
builder.add_node("agent", agent_node)
tool_node = ToolNode(tools_list)
builder.add_node("tools", tool_node)

builder.add_edge(START, "agent")

builder.add_conditional_edges(
    "agent",
    tools_condition,
)

builder.add_edge("tools", "agent")
graph = builder.compile()

if __name__ == "__main__":
    print("=" * 60)
    print("TravelBuddy - Trợ lý Du Lịch Thông Minh")
    print("Gõ 'quit' để thoát")
    print("=" * 60)

    while True:
        user_input = input("\nBạn: ").strip()
        if user_input.lower() in ("quit", "exit", "q"):
            break

        print("\nTravelBuddy đang suy nghĩ...")

        result = graph.invoke({"messages": [("human", user_input)]})
        final = result["messages"][-1]
        print(f"\nTravelBuddy: {final.content}")
