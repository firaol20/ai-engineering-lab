
from src.conversation import Conversation

conversation = Conversation(
    "You are a helpful AI assistant."
)

conversation.add_user_message("My name is Fira.")

conversation.add_assistant_message(
    "Nice to meet you, Fira!"
)

conversation.add_user_message("What is my name?")

print(conversation.get_messages())

conversation.clear_history()

print("\nAfter clearing:")
print(conversation.get_messages())
