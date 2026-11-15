# Create a new conversation.
# Add a user message.
# Add an assistant message.
# Clear conversation history.

class Conversation:
  def __init__(self, system_prompt):
    self.messages = [
      {
        "role": "system",
        "content": system_prompt
      }
    ]
  def add_user_message(self, message):
    self.messages.append({
      "role": "user",
      "content": message
    })
  def add_assistant_message(self, message):
    self.messages.append({
      "role": "assistant",
      "content": message
    })
  def clear_history(self):
    system_message = self.messages[0]
    self.messages = [system_message]
  def get_messages(self):
    return self.messages
  

  