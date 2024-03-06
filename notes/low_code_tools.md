# Low-Code/No-Code Tools for LLM

Building LLM applications is both simple and complex.

It's simple because the coding process is like building with Lego blocks. With frameworks like LangChain you can link several components into an application easily. It's complex because you still need to code. And to code, you need to study the syntax of the Python language, understand APIs of imported modules and web services, deal with package conflicts and failures, etc.

So is there a better way to build LLM applications without the need to code?

The answer is yes.

## LangChain Based Tools

Most of the low-code/no-code tools for LLM are based on LangChain. They provide a visual interface to link LLM components and pre-build APIs for common web services.

### [LangFlow](https://langflow.org/)

A drag-and-drop interface to build LLM applications. It's like a visual programming language for LLM.

![LangFlow Interface](https://miro.medium.com/v2/resize:fit:1400/1*_GPTlK4hmkMfR-uRQPem3A.png)

The application is under beta testing. You can sign up for early access on their website or deploy the [code](https://github.com/logspace-ai/langflow) on your own local machine.

### [Flowise](https://flowiseai.com/)

A YC backed startup that provides a visual interface to build LLM applications. Very similar to LangFlow.

![Flowise Interface](https://i.ytimg.com/vi/CovAPtQPU0k/maxresdefault.jpg)

You can deploy the [application](https://github.com/FlowiseAI/Flowise) on your local machine as well.

### [n8n](https://n8n.io/)

A general-purpose automation tool that turned into a LLM applications builder. It's not specifically designed for LLM, but they added LangChain and LLM related modules recently.

![n8n Interface](https://blog.cellar-c2.services.clever-cloud.com/2020/07/n8n-screenshot_w1200_q80.png)

Although their cloud service is paid, you can deploy their [community version](https://docs.n8n.io/hosting/?_gl=1*112xun1*_ga*MTk3Mzg4Mzg0My4xNzA5NzYwNzkx*_ga_0SC4FF2FH9*MTcwOTc2MDc5MS4xLjEuMTcwOTc2MDk4MC4zNi4wLjA.) on your local machine for free.

### LangFlow vs Flowise vs n8n

LangFlow and Flowise shared the same advantage: they are tailored for building LLM applications which support detailed configurations.

While n8n is rich in 3rd party integrations so it's a lot easier to integrate your LLM application with existing ecosystems.

## No-Code Agent Builder

LLM Agents is a more early-stage concept. The most popular frameworks are AutoGen from Microsoft and LangGraph from LangChain.

While LangChain has become the de facto standard for building chain-based LLM applications, AutoGen is positioning itself to be the standard of agent-based appliations. Besides the great coding framework AutoGen, Microsoft also released a No-Code interface called AutoGen Studio for building agents.

### AutoGen Studio

![AutoGen Studio](https://microsoft.github.io/autogen/assets/images/autogenstudio_home-cce78dc150d1bb0073620754df73d863.png)

AutoGen Studio is currently in beta testing. But the current release has showed impressive ability to build agents without coding. Empowered by OpenAI's GPT models, agents in AutoGen can not only use tools and but also develop tools for further usages.

## LangChain Expression Language

While No-Code tools seems easy to use at first glance, their advantage in visual programming can backfire when you need to deal with complex data processing. And since the LLM industry is evolving rapidly, using visual programming tools means months behind the latest features.

So why don't we just code.

LangChain Expression Language (LCEL) provides a beautiful balance between the flexibility and the simplicity. It's a domain-specific language for building LLM applications. Check this impressive comparison between a LLM application using [LCEL and plain Python](https://python.langchain.com/docs/expression_language/why#full-code-comparison).

```Python
# LCEL Example Code

prompt = ChatPromptTemplate.from_template("tell me a short joke about {topic}")
model = ChatOpenAI(model="gpt-4")
output_parser = StrOutputParser()

chain = prompt | model | output_parser

chain.invoke({"topic": "ice cream"})
```

## Final Thoughts

As much as I love No-Code tools, LCEL is my pick for now. I hope the No-Code tools can cover more use cases and provide more flexibility in the future.

Check this note for a detailed guide on [LangChain Expression Language](./notes/langchain_expression_language.md)
