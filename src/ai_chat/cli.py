import typer

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
    print(f"Model: {model}")
    print(f"System prompt: {system_prompt}")


if __name__ == "__main__":
    app()
