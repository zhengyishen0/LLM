[AutoGen](https://microsoft.github.io/autogen/docs/Getting-Started)
[AutoGenStudio](https://microsoft.github.io/autogen/blog/2023/12/01/AutoGenStudio/)
[Ollama Models](https://ollama.ai/library)
[Code Interpreter](https://github.com/KillianLucas/open-interpreter)
[LM Studio](https://lmstudio.ai/)
[Gradio](https://www.gradio.app/)
[Streamlit](https://streamlit.io/)
[HuggingFace](https://huggingface.co/transformers/)
[Colab Ollama](https://colab.research.google.com/drive/1f2qELQboeqr1zPaOABe0WX0_YLbN_KJm#scrollTo=5YzWGOv-0k7s)

```zsh
export OLLAMA_HOST=...
echo $OLLAMA_HOST

ollama run mistral
```

````zsh
autogenstudio ui --port 8081


```zsh
pip freeze > requirements.txt
pip install -r requirements.txt
````

```zsh
conda create -n llm python=3.10
conda env list
conda env remove --name llm

conda activate llm
conda deactivate
```
