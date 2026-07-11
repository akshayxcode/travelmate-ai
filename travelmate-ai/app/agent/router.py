from app.prompts.travel_prompt import SYSTEM_PROMPT
from app.services.ollama_service import OllamaService
from app.services.memory_service import MemoryService


class TravelRouter:

    @staticmethod
    def process(message: str):
        session_id = "default"
         
        # 1. Save the user's message
        MemoryService.save(session_id, "user", message)

        # 4. Ask Qwen to format the response
        prompt = f"{SYSTEM_PROMPT}\nUser: {message}"
        response = OllamaService.ask(prompt)

        # 5. Save the assistant's response
        MemoryService.save(session_id, "assistant", response)

        return response