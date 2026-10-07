from pathlib import Path

DEFAULT_SYSTEM_PROMPT = "You are a helpful assistant."


def get_config_path() -> Path:
    return Path.home() / ".ai-chat" / "config.txt"


def load_or_create_config() -> str:
    config_path = get_config_path()
    config_path.parent.mkdir(parents=True, exist_ok=True)

    try:
        with config_path.open("x", encoding="utf-8") as config_file:
            config_file.write(DEFAULT_SYSTEM_PROMPT)
    except FileExistsError:
        pass

    with config_path.open("r", encoding="utf-8") as config_file:
        return config_file.read()
