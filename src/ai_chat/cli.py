import asyncio
import sys
from pathlib import Path

import httpx
import typer

if __package__:
    from .core import main as run_chat_loop
else:
    sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
    from ai_chat.core import main as run_chat_loop

app = typer.Typer()


@app.callback()
def main() -> None:
    pass


@app.command()
def chat(
    model: str = typer.Option("llama3", help="Model to use for the conversation."),
    system_prompt: str = typer.Option(
        "You are a helpful assistant.",
        help="System prompt for the conversation.",
    ),
) -> None:
    try:
        asyncio.run(run_chat_loop(model, system_prompt))
    except httpx.ConnectError:
        print("Can't reach Ollama. Is it running? Try: ollama serve")


if __name__ == "__main__":
    app()
