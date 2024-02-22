from langchain.schema import StrOutputParser
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.runnables import RunnablePassthrough
from langchain_openai import ChatOpenAI


function = {
    "name": "solver",
    "description": "Formulates and solves an equation",
    "parameters": {
        "type": "object",
        "properties": {
            "equation": {
                "type": "string",
                "description": "The algebraic expression of the equation",
            },
            "solution": {
                "type": "string",
                "description": "The solution to the equation",
            },
        },
        "required": ["equation", "solution"],
    },
}

tools = [
    {
        "type": "function",
        "function": {
            "name": "get_current_weather",
            "description": "Get the current weather in a given location",
            "parameters": {
                "type": "object",
                "properties": {
                    "location": {
                        "type": "string",
                        "description": "The city and state, e.g. San Francisco, CA",
                    },
                    "unit": {"type": "string", "enum": ["celsius", "fahrenheit"]},
                },
                "required": ["location"],
            },
        },
    }
]

# Need gpt-4 to solve this one correctly
prompt = ChatPromptTemplate.from_messages(
    [
        (
            "system",
            "Write out the following equation using algebraic symbols then solve it.",
        ),
        ("human", "{input}"),
    ]
)

model = ChatOpenAI(model="gpt-4", temperature=0).bind(
    tools=tools  # function_call={"name": "solver"}, functions=[function]
)

runnable = (
    {"input": RunnablePassthrough()}
    | prompt
    | model  # .bind(stop="SOLUTION")
    # | StrOutputParser()
)

message = "What's the weather in SF, NYC and LA?"
print(runnable.invoke(message))
