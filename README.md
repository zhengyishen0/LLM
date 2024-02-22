# LLM in Plain English

> My study notes on LLM and its applications

## Get Started

When you first start learning about LLM, you'll be overwhelmed by the amount of information available.

So where should you start?
What's the learning path?

This GitHub repo stores all the notes on my study of LLM and its applications. The goal is to guide you into the realm of LLM in the least amount of time, so you can begin your own exploration and development with confidence.

We're going to cover the following topics:

- [Large Language Models](#large-language-models)(OpenAI, Gemini, Claude, and Open source LLMs)
- [Prompt Engineering](#prompt-engineering) (Few-Shot, Zero-Shot, CoT, RAG, ReAct, etc)
- [Developer Tools](#developer-tools) (HuggingFace, Colab, Ollama, LM Studio, Flowsie, n8n, etc)
- [Chains & Agents](#chains--agents) (LangChain, LangGraph, AutoGen, AutoGPT, etc)
- [Python Coding](#python-coding) (Environment setup, snippets, etc)
- [Resources](#resources) (Website, Books, papers, articles, etc)

## To Be Continued...

- [ ] Thoughts on chatmodels, chains, and agents
- [ ] OpenAI assistant
- [ ] LangChain Expression Language
- [ ] Low-code Tools: Flowise, LangFlow, n8n
- [ ] zsh code to shell file
- [ ] Python Function -> Tool -> OpenAI Functions
- [ ] Chat Completion -> Chat Model -> Agent

## Python Coding

### Preparation

This tutorial assumes you have the basic knowledge of Python. You should at least know how use Jupter Notebook, run Python script in VSCode, and install Python packages using pip.

#### Create Virtual Environment.

> I didn't follow this step first and wasted hours of time debugging the package conflicts. So don't skip.

Simply copy and paste the following commands into your terminal.

```zsh
conda create -n llm python=3.10  # 3.10 is the latest working version, do not use 3.11 or higher.
conda activate llm  # llm is the name of the virtual environment, you can use any name you like.
```

Other commands you might need:

```zsh
conda env list  # list all the virtual environments
conda env remove --name llm  # remove the virtual environment named "llm"
conda deactivate  # deactivate the current virtual environment
```

#### Install Packages

Copy the `requirements.txt` file into your project folder and run the following command

```zsh
pip install -r requirements.txt
```

To keep a clear record of the packages you've installed, you can run the following command to update the `requirements.txt` file after you use `pip install`.

```zsh
pip freeze > requirements.txt
```

If you're lazy like me, you can also use my shortcut. Just run the following command in your terminal.

```zsh
# Automatically update the `requirements.txt` file after installing packages.
# The function name "pipinstall" is the shortcut name. Replace it with any you like.
echo 'function pipinstall() {
    pip install "$@"
    pip freeze > requirements.txt
}' >> ~/.zshrc  # or ~/.bashrc if you're using bash

source ~/.zshrc
```

Next time, instead of running `pip install your-package-name`, run this.

```zsh
pipinstall your-package-name
```

#### Using Ollama

Ollama is a powerful tool for LLM development. Download it from [here](https://ollama.ai/).

Then in your terminal, you can start using open-sourced LLMs like this.

```zsh
ollama run mistral  # Replace "mistral" with the model name, Ollama will download the model and run it for you.
```

Other userful commands:

```zsh
ollama list  # list all the available models
ollama rm mistral  # remove the model named "mistral"
```

**Use Colab GPU to run Ollama**
LLM requires a lot of computation power. My M1 Macbook Air gets so slow running a small model locally. But thanks to the generous Google, you can use their GPU for free.

Copy this [Colab Notebook](/ollama.ipynb) to your Colab and follow the instructions.

Once you get the `ngrok` server running, copy the endpoint and use this command.

```zsh
export OLLAMA_HOST=your-ngrok-endpoint
ollama
```

And then you can use ollama as usual.

If you're tired of adding the `export` command every time you open a new terminal, you can use this shortcut.

```zsh
echo 'function collama() {
  export OLLAMA_HOST="$@"
}' >> ~/.zshrc

source ~/.zshrc
```

Next time.

```zsh
collama paste-ngrok-endpoint
```

Done!

## Prompt Engineering

Prompt Engineering has been a hot topic in the LLM community, and there are an ocean of resources available to learn about it. Among all, I found this [website](https://www.promptingguide.ai/) to be the most helpful to me.

We've new prompting techniques coming out almost every day. After spending 8 hours learning all the new techniques and reading papers, I've found that the followings are the only must-read. I'll try to explain these concepts in plain English.

### Few-Shot Prompting

> For example...

The concept of few shot prompting is simple. You give a few examples of the task you want the model to perform, and the model will perform the task for you.

### Zero-Shot Prompting

> Quick question...

This is not necessarily a technique. It's just the very basic form of prompting: you ask a question, the model replies an answer. This concept differentiate itself from `few-shot prompting` that it requires no example.

### Chain of Thought (CoT)

> Step-by-step...

This is the famous "think step-by-step" method. You append the "think step-by-step" instruction to your question and the model's performance will be improved magically.

### Retreival Augmented Generation (RAG)

> According to...

RAG can be considered as an extension of the `few-shot prompting`. It's a technique that allows the model to retrieve information from a database and generate a response based on the retrieved information.

**RAG vs Fine-Tuning**

_TL;DR: For beginner LLM developer, you should always prefer RAG over fine-tuning._

RAG is better at using the up-to-date knowledge without retraining the model. Fine-tuning is better at creating specialized LLMs using smaller models. (Deep Dive [Here](https://www.promptingguide.ai/research/rag.en#rag-vs-fine-tuning))

### ReAct

> Think and act...

ReAct extend the idea of `Chain of Thought (CoT)` from the trace of reasoning to action. By taking action, the model can correct its reasoning by using the feedback from the observation of the action.

## Resources

- [AutoGen](https://microsoft.github.io/autogen/docs/Getting-Started)
- [AutoGenStudio](https://microsoft.github.io/autogen/blog/2023/12/01/AutoGenStudio/)
- [Ollama Models](https://ollama.ai/library)
- [Code Interpreter](https://github.com/KillianLucas/open-interpreter)
- [LM Studio](https://lmstudio.ai/)
- [Gradio](https://www.gradio.app/)
- [Streamlit](https://streamlit.io/)
- [HuggingFace](https://huggingface.co/transformers/)
- [Colab Ollama](https://colab.research.google.com/drive/1f2qELQboeqr1zPaOABe0WX0_YLbN_KJm#scrollTo=5YzWGOv-0k7s)

<!-- ```zsh
autogenstudio ui --port 8081
``` -->

## Next Week

- [x] Study [LangChain Modules](https://python.langchain.com/docs/modules/)
- [ ] Practice: Document Agent
- [ ] Open Sourced Models: Mistral, Llama, Open Interpreter
- [ ] LangChain [Debugging](https://python.langchain.com/docs/guides/debugging) and [Fallbacks](https://python.langchain.com/docs/guides/fallbacks)

## Project H.E.R

**Agent model**

- [ ] Conversation starter detection
- [ ] Conversation ender

**Voice**

- [ ] Text-to-Voice
- [ ] Whisper (Voice-to-Text)
- [ ] Attention Recaller
- [ ] Audio Streaming

**3rd Party API**

- [ ] Documentation Finder
- [ ] API Builder (e.g. Uber)
- [ ] 3rd-party Service login interface
- [ ] Adaptive Visual Interface (map, list view)
