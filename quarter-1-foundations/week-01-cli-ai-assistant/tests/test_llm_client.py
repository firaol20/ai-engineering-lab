
from src.llm_client import LLMClient


# Create our LLM client
client = LLMClient()

# Prepare a test message
messages = [
    {
        "role": "user",
        "content": "Explain what an API is in two simple sentences."
    }
]

# Send the message and receive the response
answer = client.generate_response(messages)

print("\nAI Response:")
print(answer)
