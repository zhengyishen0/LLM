# Prompt Engineering

Prompt Engineering has been a hot topic in the LLM community, and there are an ocean of resources available to learn about it. Among all, I found this [website](https://www.promptingguide.ai/) to be the most helpful to me.

We've new prompting techniques coming out almost every day. After spending 8 hours learning all the new techniques and reading papers, I've found that the followings are the only must-read. I'll try to explain these concepts in plain English.

## Few-Shot Prompting

> For example...

The concept of few shot prompting is simple. You give a few examples of the task you want the model to perform, and the model will perform the task for you.

## Zero-Shot Prompting

> Quick question...

This is not necessarily a technique. It's just the very basic form of prompting: you ask a question, the model replies an answer. This concept differentiate itself from `few-shot prompting` that it requires no example.

## Chain of Thought (CoT)

> Step-by-step...

This is the famous "think step-by-step" method. You append the "think step-by-step" instruction to your question and the model's performance will be improved magically.

## Retreival Augmented Generation (RAG)

> According to...

RAG can be considered as an extension of the `few-shot prompting`. It's a technique that allows the model to retrieve information from a database and generate a response based on the retrieved information.

**RAG vs Fine-Tuning**

_TL;DR: For beginner LLM developer, you should always prefer RAG over fine-tuning._

RAG is better at using the up-to-date knowledge without retraining the model. Fine-tuning is better at creating specialized LLMs using smaller models. (Deep Dive [Here](https://www.promptingguide.ai/research/rag.en#rag-vs-fine-tuning))

## ReAct

> Think and act...

ReAct extend the idea of `Chain of Thought (CoT)` from the trace of reasoning to action. By taking action, the model can correct its reasoning by using the feedback from the observation of the action.
