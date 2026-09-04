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


def main() -> None:
    config = ChatConfig()
    history: list[ChatMessage] = [ChatMessage(role="system", content=config.system_prompt)]
    print("Chatbot ready. Type 'quit' to exit.")
    while True:
        user_input = input("You: ")
        if user_input.lower() == "quit":
            break
        history.append(ChatMessage(role="user", content=user_input))
        dict_messages = [{"role": m.role, "content": m.content} for m in history]
        reply = send_request(dict_messages, config.model)
        print("Bot:", reply)
        history.append(ChatMessage(role="assistant", content=reply))


if __name__ == "__main__":
    main()
