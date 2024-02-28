
# Update requirements.txt after pip install
echo 'function pipinstall() {
    pip install "$@"
    pip freeze > requirements.txt
}' >> ~/.zshrc  # or ~/.bashrc if you're using bash

# Using Colab GPU for Olllama
echo 'function collama() {
  export OLLAMA_HOST="$@"
}' >> ~/.zshrc

# how-to: collama paste-ngrok-endpoint

source ~/.zshrc