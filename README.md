# ai-chat

A lightweight command-line chatbot that connects to a local Ollama instance.

## Install

From the project directory, install the package in editable mode:

```bash
pip install -e .
```

Make sure Ollama is installed and running, and that the model you want to use has
been pulled.

## Usage

See the available commands and options:

```bash
ai-chat --help
```

Start a chat with the default `llama3` model:

```bash
ai-chat chat --model llama3 --system-prompt "You are a helpful assistant."
```

Type `quit` to end the conversation.

## Why this project exists

This project is being built while learning modern Python and AI engineering
fundamentals, including packaging, command-line interfaces, asynchronous code,
and integrating with a local language model.
