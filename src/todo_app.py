from pathlib import Path

import typer

TODO_FILE = Path("todo.txt")
app = typer.Typer()


@app.command()
def add(item: str) -> None:
    with TODO_FILE.open("a", encoding="utf-8") as todo_file:
        todo_file.write(f"{item}\n")


@app.command()
def list_items() -> None:
    with TODO_FILE.open("r", encoding="utf-8") as todo_file:
        for line in todo_file:
            print(line.rstrip("\n"))


if __name__ == "__main__":
    app()
