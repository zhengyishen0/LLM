from langgraph.prebuilt import ToolInvocation, ToolExecutor
from langchain_core.messages import ToolMessage
from functools import partial
import json


tool_indicator = "tool_calls"  # "function_call"

# Define the function that determines whether to continue or not


def should_continue(state):
    messages = state['messages']
    last_message = messages[-1]
    # If there is no function call, then we finish
    if tool_indicator not in last_message.additional_kwargs:
        return "end"
    else:
        return "continue"

# Define the function that calls the model


def use_model_state(model, state):
    messages = state['messages']
    response = model.invoke(messages)
    return {"messages": [response]}


def call_model(model):
    return partial(use_model_state, model)
# Define the function that calls the model


def call_agent(agent, chat, state):
    messages = state['messages']
    response = agent.invoke(
        {"input": messages[0], "chat_history": chat.history})
    return {"messages": [response['output']]}

# Define the function to execute tools


def use_tool_state(tools, state):
    messages = state['messages']
    last_message = messages[-1]

    tool = last_message.additional_kwargs[tool_indicator][0]
    action = ToolInvocation(
        tool=tool['function']["name"],
        tool_input=json.loads(tool['function']['arguments'])
    )

    tool_executor = ToolExecutor(tools)

    response = tool_executor.invoke(action)
    function_message = ToolMessage(
        content=str(response), tool_call_id=tool['id'])
    return {"messages": [function_message]}


def call_tools(tools):
    return partial(use_tool_state, tools)
