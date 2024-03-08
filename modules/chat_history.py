from langchain_core.messages import AIMessage, HumanMessage, SystemMessage, ToolMessage, FunctionMessage


class ChatHistory:

    def __init__(self, system_message=None):
        system_message = system_message or "You are a helpful assistant."

        self.system_message = SystemMessage(content=system_message)
        self.history = [self.system_message]

    def update(self, message: dict):
        if 'input' in message:
            self.history.append(HumanMessage(content=message['input']))
        self.history.append(AIMessage(content=message['output']))
        return message

    def reset(self):
        self.history = [self.system_message]
