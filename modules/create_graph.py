from langchain_core.messages import HumanMessage
from langgraph.graph import StateGraph, END
from typing import TypedDict, Annotated, Sequence
import operator
from langchain_core.messages import BaseMessage


class AgentState(TypedDict):
    messages: Annotated[Sequence[BaseMessage], operator.add]


def create_graph(nodes: list[dict]):
    """
    sample input
    nodes = [
        {"name":"agent", "node": call_model}, 
        {"name":"action", "node": call_tool, "condition": should_continue}
        ]
    """

    graph = StateGraph(AgentState)

    entry = nodes[0]['name']
    for node in nodes:
        graph.add_node(node['name'], node['node'])

    graph.set_entry_point(entry)

    for node in [n for n in nodes if 'condition' in n.keys()]:
        graph.add_conditional_edges(entry, node["condition"],
                                    {
            "continue": node["name"],
            "end": END
        }
        )

    for node in nodes[1:]:
        graph.add_edge(node['name'], entry)
    # graph.add_edge('action', 'agent')

    return graph.compile()


def stream_app(app, user_input):
    inputs = {"messages": [HumanMessage(content=user_input)]}
    for output in app.stream(inputs):
        # stream() yields dictionaries with output keyed by node name
        for key, value in output.items():
            print(f"Output from node '{key}':")
            print("---")
            print(value)
        print("\n---\n")
