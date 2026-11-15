from src.conversation import Conversation
from src.llm_client import LLMClient


def main():
    # Initialize our components
    conversation = Conversation(
        "You are a helpful AI assistant."
    )

    llm_client = LLMClient()

    print("AI Assistant is ready!")
    print("Type /clear to reset conversation.")
    print("Type /exit to quit.\n")

    while True:
        user_message = input("You: ")

        if not user_message:
            continue

        if user_message == "/exit":
            print("\nAI: Goodbye! 👋")
            break

        if user_message == "/clear":
            conversation.clear_history()
            print("Conversation history cleared.")
            continue

        conversation.add_user_message(user_message)

        try:
            print("\nAI: ", end="", flush=True)

            response_parts = []

            for chunk in llm_client.stream_response(
                conversation.get_messages()
            ):
                print(chunk, end="",flush=True)
                response_parts.append(chunk)

            answer = "".join(response_parts)

            print("\n")

            conversation.add_assistant_message(answer)


        except Exception as error:
            print(f"\nError: {error}\n")


if __name__ == "__main__":
    main()
