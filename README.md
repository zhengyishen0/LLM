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
export OPENAI_API_KEY=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
export OLLAMA_HOST=https://ae7d-34-69-17-127.ngrok-free.app/
echo $OLLAMA_HOST

autogenstudio ui --port 8081

ollama run mistral

conda activate pyautogen
litellm --model ollama/mistral

npx n8n

pip freeze > requirements.txt
pip install -r requirements.txt


conda create -n llm python=3.10
conda env list
conda env remove --name llm
conda activate llm


```
