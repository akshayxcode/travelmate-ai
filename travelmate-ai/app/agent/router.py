from app.prompts.travel_prompt import SYSTEM_PROMPT
from app.services.ollama_service import OllamaService


class TravelRouter:

    @staticmethod
    def process(message: str):

        prompt = f"""
{SYSTEM_PROMPT}

User:

{message}
"""

        return OllamaService.ask(prompt)