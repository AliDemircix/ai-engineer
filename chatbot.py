# chatbot.py
import requests
from dataclasses import dataclass

URL = "http://localhost:11434/api/chat"


@dataclass
class ChatMessage:
    role: str
    content: str


@dataclass
class ChatConfig:
    model: str = "llama3"
    max_history: int = 8
    system_prompt: str = "You are a helpful assistant."


def send_request(messages: list[dict[str, str]], model: str) -> str:
    """
    messages: a list of role/content dicts (the shape from Part 3)
    returns: the model's reply text (str)
    """
    response = requests.post(
        URL,
        json={"model": model, "messages": messages, "stream": False},
    )
    data = response.json()
    return data["message"]["content"]


def build_messages(config: ChatConfig, history: list[ChatMessage]) -> list[dict[str, str]]:
    """
    config: carries system_prompt and max_history
    history: every ChatMessage so far
    returns: the dict list Ollama expects
    """
    system_message = ChatMessage(role="system", content=config.system_prompt)
    trimmed_history = history[-config.max_history:]
    combined = [system_message] + trimmed_history
    return [{"role": m.role, "content": m.content} for m in combined]


def main() -> None:
    config = ChatConfig()
    history: list[ChatMessage] = []
    print("Chatbot ready. Type 'quit' to exit.")
    while True:
        user_input = input("You: ")
        if user_input.lower() == "quit":
            break
        history.append(ChatMessage(role="user", content=user_input))
        messages = build_messages(config, history)
        reply = send_request(messages, config.model)
        print("Bot:", reply)
        history.append(ChatMessage(role="assistant", content=reply))


if __name__ == "__main__":
    main()
