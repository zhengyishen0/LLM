# LLM in Python

## Preparation

This tutorial assumes you have the basic knowledge of Python. You should at least know how use Jupyter Notebook, run Python script in VSCode, and install Python packages using pip.

### Create Virtual Environment.

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

### Install Packages

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

### Using Ollama

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
