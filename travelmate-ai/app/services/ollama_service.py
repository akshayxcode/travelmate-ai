from ollama import Client

from app.config import MODEL_NAME, OLLAMA_URL


class OllamaService:

    @staticmethod
    def ask(prompt: str):
        client = Client(host=OLLAMA_URL)

        response = client.chat(
            model=MODEL_NAME,
            messages=[
                {
                    "role": "user",
                    "content": prompt
                }
            ],
            options={
                "num_predict": 2048,
                "temperature": 0.7
            }
        )

        return response["message"]["content"]