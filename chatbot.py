# chatbot.py
import requests

URL = "http://localhost:11434/api/chat"
MODEL = "llama3"
SYSTEM_PROMPT = "You are a helpful assistant."


def send_request(messages):
    """
    messages: a list of role/content dicts (the shape from Part 3)
    returns: the model's reply text (str)
    """
    response = requests.post(
        URL,
        json={"model": MODEL, "messages": messages, "stream": False},
    )
    data = response.json()
    return data["message"]["content"]


def main():
    messages = [{"role": "system", "content": SYSTEM_PROMPT}]
    print("Chatbot ready. Type 'quit' to exit.")
    while True:
        user_input = input("You: ")
        if user_input.lower() == "quit":
            break
        messages.append({"role": "user", "content": user_input})
        reply = send_request(messages)
        print("Bot:", reply)
        messages.append({"role": "assistant", "content": reply})


if __name__ == "__main__":
    main()
