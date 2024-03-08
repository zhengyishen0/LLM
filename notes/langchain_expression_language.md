# LangChain Expression Language

LangChain Expression Language (LCEL) is a high-level abstraction of using LLM models. Check out this impressive comparison between a LLM application using [LCEL and plain Python](https://python.langchain.com/docs/expression_language/why#full-code-comparison).

With LCEL, you can build a LLM application with a few lines of code that are intuitive and easy to understand.

```Python
# LCEL Example Code

prompt = ChatPromptTemplate.from_template("tell me a short joke about {topic}")
model = ChatOpenAI(model="gpt-4")
output_parser = StrOutputParser()

chain = prompt | model | output_parser

chain.invoke({"topic": "ice cream"})
```

Compare with a similar function designed in a No-Code tool:

![LangFlow Interface](https://miro.medium.com/v2/resize:fit:1400/1*_GPTlK4hmkMfR-uRQPem3A.png)

## Basic Concepts

To make the most of LCEL, you need to understand some basic concepts:

**Runnable**

Runnable is the basic building block in LCEL. Everything in LCEL is a runnable.

A runnable can be a prompt, a model, a parser, or a chain of runnables. Every runnable can use the method of [`invoke`, `stream`, and `batch`](https://python.langchain.com/docs/expression_language/interface) to run the model.

This design makes LangChain outcompete other frameworks with extreme simplicity.

**Chain**:

Chain, as the package name LangChain suggests, is the most important concept in LCEL.

In LangChain, a chain is a sequence of "runnables" that can be called like a ChatGPT. It is the LLM application that you want to build.

A very basic chain looks like this:

```Python
chain = prompt | model | output_parser
```

LangChain also provides an option to run multiple chains in parallel. Here is an example of a RAG chain that uses multiple chains in parallel:

```Python
# Define a RAG chain
vectorstore = FAISS.from_texts(["context data..."], embedding=OpenAIEmbeddings())
retriever = vectorstore.as_retriever()
template = "Based on the following context:{context}, answer the question: {question}"
prompt = ChatPromptTemplate.from_template(template)
model = ChatOpenAI()

chain = (
    {"context": retriever, "question": RunnablePassthrough()} # this is equivalent to RunnableParallel(context=retriever, question=RunnablePassthrough())
    | prompt
    | model
    | StrOutputParser()
)

# Run the chain
chain.invoke("...")

# Display a visual representation of the chain
chain.get_graph().print_ascii()
```

```
           +---------------------------------+
           | Parallel<context,question>Input |
           +---------------------------------+
                    **               **
                 ***                   ***
               **                         **
+----------------------+              +-------------+
| VectorStoreRetriever |              | Passthrough |
+----------------------+              +-------------+
                    **               **
                      ***         ***
                         **     **
           +----------------------------------+
           | Parallel<context,question>Output |
           +----------------------------------+
                             *
                             *
                             *
                  +--------------------+
                  | ChatPromptTemplate |
                  +--------------------+
                             *
                             *
                             *
                      +------------+
                      | ChatOpenAI |
                      +------------+
                             *
                             *
                             *
                   +-----------------+
                   | StrOutputParser |
                   +-----------------+
                             *
                             *
                             *
                +-----------------------+
                | StrOutputParserOutput |
                +-----------------------+
```

**Agent**:

While a chain is bascially a chat bot, an agent is a chat bot equipped with tools.

```Python

### Pseudo code

llm = ChatOpenAI()
tools = [function_1, function_2, function_3, ...]
chain = (
        RunnablePassthrough.assign(
            agent_scratchpad=lambda x: format_to_openai_tool_messages(  # Convert the usage of tools to OpenAI tool format
                x["intermediate_steps"]
            )
        )
        | prompt
        | llm.bind(tools=[convert_to_openai_tool(tool) for tool in tools])  # Convert the tools to OpenAI tool format
        | OpenAIToolsAgentOutputParser()
    )

agent = AgentExecutor(agent=chain, tools=tools)  # AgentExecutor wraps a chain and tools into a runnable object
```

LCEL provides a convenient way to turn a custom Python function into a tool for OpenAI APIs.

Though many open sourced LLMs support the use of tools, OpenAI is by far the most advanced model that can use multiple tools in a single chain.

So, I rewrite the `create_openai_tools_agent` module in LangChain into [openai_agent](../modules/openai_agent.py) that can generate a OpenAI agent (with memory) without going through all the hassle.

This is how easy it is to create an OpenAI agent with the module:

```Python
from modules.openai_agent import create_agent

agent = create_agent(prompt=prompt, tools=tools)
agent.invoke({"input": user_input})
```

If you want to create an agent with memory, check out this [example](../agent.ipynb).

**Graph**

The LangChain team doesn't satisfied with their current achievement in "Chains". They are looking at the future of autonomous AI. Read this blog for deep insights: [LangGraph for Code Generation](https://blog.langchain.dev/code-execution-with-langgraph/).

LangGraph is like a maze maker. You define the spots available (nodes), and the possible paths between them (edges). Then, the model will find a path from the entry to the goal going through the nodes and edges you defined.

You can find my example code here: [LangGraph Example Code](../graph.ipynb).

## LCEL Modules

We can also add Python functions into a chain as runnables.

`To Be Continued...`

## When Not to Use LCEL

Although LCEL provides a beautiful interface to work with LLM models and relative APIs, it's not always the best choice to use the native modules from LangChain (IMHO).

Because at the basics, LCEL is just a wrapper around the OpenAI (and other LLMs') APIs. Sometimes, it's just easier (to understand and to code) to use plain Python without the need to refer to the LCEL documentation.

For example, if we want to add memory to a chat bot automatically, this is what LangChain suggests:

```Python
from langchain_community.chat_message_histories import ChatMessageHistory
from langchain_core.chat_history import BaseChatMessageHistory
from langchain_core.runnables.history import RunnableWithMessageHistory

store = {}


def get_session_history(session_id: str) -> BaseChatMessageHistory:
    if session_id not in store:
        store[session_id] = ChatMessageHistory()
    return store[session_id]


# Wrap the runnable with the message history
with_message_history = RunnableWithMessageHistory(
    chain,  # Assume we've already defined the chain
    get_session_history,
    input_messages_key="input",
    history_messages_key="history",
)

# Now use the Chat Model with memory
with_message_history.invoke(
    {"input": user_input},
    config={"configurable": {"session_id": "abc123"}},
)

```

Here's my version of the same memory capability:

```Python
# ./modules/chat_history.py
from langchain_core.messages import AIMessage, HumanMessage, SystemMessage


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


# Your main file
from modules.chat_history import ChatHistory

# Add memory to a chat model
chat = ChatHistory("Welcome to the chat!")  # Start with a system message
chat_with_memory = chain | RunnableLambda(chat.update)  # Update the chat history with each response
chat_with_memory.invoke({"input": user_input, "chat_history": chat.history})

# This ChatHistory class adds the memory capability to the chat model and also expose the possibility to manipulate the chat history outside the chain of runnables.

```
