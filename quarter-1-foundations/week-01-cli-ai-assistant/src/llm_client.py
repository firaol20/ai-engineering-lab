
import os
import json
import requests
from dotenv import load_dotenv

load_dotenv()

class LLMClient:
    def __init__(self):
        self.api_key = os.getenv("OPENROUTER_API_KEY")
        self.model = os.getenv("OPENROUTER_MODEL")

        if not self.api_key:
            raise ValueError("OPENROUTER_API_KEY is missing.")

        if not self.model:
            raise ValueError("OPENROUTER_MODEL is missing.")

        self.base_url = "https://openrouter.ai/api/v1/chat/completions"

    def generate_response(self, messages):
        headers = {
            "Authorization": f"Bearer {self.api_key}",
            "Content-Type": "application/json"
        }

        payload = {
            "model": self.model,
            "messages": messages
        }

        response = requests.post(
            self.base_url,
            headers=headers,
            json=payload,
            timeout=60
        )

        response.raise_for_status()

        data = response.json()

        return data["choices"][0]["message"]["content"]

    def stream_response(self, messages):
        headers = {
            "Authorization": f"Bearer {self.api_key}",
            "Content-Type": "application/json"
        }

        payload = {
            "model": self.model,
            "messages": messages,
            "stream": True
        }

        with requests.post(
            self.base_url,
            headers=headers,
            json=payload,
            stream=True,
            timeout=(15, 120)
        ) as response:

            response.raise_for_status()

            for line in response.iter_lines():
                if not line:
                    continue

                line = line.decode("utf-8")

                if not line.startswith("data: "):
                    continue

                data = line[6:]

                if data == "[DONE]":
                    break

                chunk = json.loads(data)

                choices = chunk.get("choices", [])

                if not choices:
                    continue

                content = choices[0].get(
                    "delta", {}
                ).get("content")

                if content:
                    yield content