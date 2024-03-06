# Basic Concepts

The concepts in the LLM world are sometimes confusing. This section will try to answer the most common questions people may have when they start learning about LLM.

## LLM Model vs Chat Completion Model

LLM models are essential a text generators. They are trained to generate text based on a given prompt.

> Prompt: **_The sky is..._**
>
> Generated Text: **_blue._**

A chat completion model is trained on top of a LLM model with the aim of responding in conversations.

> ChatGPT is a chat completion model based on GPT-3 with memory capability.

## Chat Completion vs Assistant (OpenAI)

Assistants are chat completion models with additional capabilities such as role-assignment, tools, and context.

You can assign a role to an assistant and instruct its behavior based on the role.

You can give an assistant tools to perform specific tasks such as calling APIs and running certain functions.

You can also provide information for the assistant to refer to during the conversation ([RAG](prompt_engineering.md#retreival-augmented-generation-rag)).

## Tools and Functions (OpenAI)

Tools and functions are the capabilities that you can give to an assistant to perform specific tasks. They are very similar concepts. For older model from OpenAI, they can only use one given tool at a time, that tool is called "Functions". For the newer models, they can use multiple tools at the same time.

## Chains vs Agents

Chains and agents are two ways of programming LLMs.

Chains take LLMs as workers on an assembly line. Though the assembly line can be complex that has conditions (if-else) and loops (for-while), the workers are doing a predictable job. This is the concept of "**Model as a Service**".

In a "chain" framework, LLMs are the one to decide which tool to use, when to use, and how to use.

When there are multiple models involved, they are connected in [DAG](https://en.wikipedia.org/wiki/Directed_acyclic_graph). This implementation is powerful enough to solve most problems.

But agents take LLMs implementation to the next level. Agents want LLMs to be managers, who are capable of not only doing the job but also making decisions.

In a agent framework, LLMs are the one to decide how to solve the task and when the task is finished. This implementation is more flexible and powerful, but also more complex and harder to control.

[AutoGPT](https://github.com/Significant-Gravitas/AutoGPT), [BabyAGI](https://github.com/yoheinakajima/babyagi), [LangGraph](https://blog.langchain.dev/langgraph/) and [AutoGen](https://microsoft.github.io/autogen/) and the few framework pioneered in this domain.
