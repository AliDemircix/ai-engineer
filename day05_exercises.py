import anthropic

client = anthropic.Anthropic()
user_message = [{"role": "user", "content": "What is a variable?"}]

with_system_prompt = client.messages.create(
    model="claude-haiku-4-5",
    max_tokens=150,
    system="You are a grumpy teacher who gives short, blunt answers.",
    messages=user_message,
)
print("With system prompt:")
print(with_system_prompt)

without_system_prompt = client.messages.create(
    model="claude-haiku-4-5",
    max_tokens=150,
    messages=user_message,
)
print("Without system prompt:")
print(without_system_prompt)
