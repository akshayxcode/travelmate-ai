import os
import sys
import unittest
from unittest.mock import patch
from fastapi.testclient import TestClient

# Add travelmate-ai directory to system path
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

from app.main import app


class TestTravelMate(unittest.TestCase):

    def setUp(self):
        self.client = TestClient(app)

    @patch("app.services.ollama_service.OllamaService.ask")
    def test_chat_endpoint(self, mock_ask):
        # Setup mock response
        mock_ask.return_value = "Hello! I am TravelMate AI, your friendly travel assistant."

        # Send request
        response = self.client.post("/chat", json={"message": "Suggest a trip to Paris"})

        # Assertions
        self.assertEqual(response.status_code, 200)
        data = response.json()
        self.assertIn("response", data)
        self.assertEqual(data["response"], "Hello! I am TravelMate AI, your friendly travel assistant.")
        
        # Verify the prompt contents
        mock_ask.assert_called_once()
        called_prompt = mock_ask.call_args[0][0]
        self.assertIn("Suggest a trip to Paris", called_prompt)
        self.assertIn("TravelMate AI", called_prompt)


if __name__ == "__main__":
    unittest.main()
