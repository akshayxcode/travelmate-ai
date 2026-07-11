import re


class Planner:

    @staticmethod
    def decide(message: str):
        message_lower = message.lower()
        
        # 1. Determine tool name
        tool = None
        if "budget" in message_lower or "cost" in message_lower or "price" in message_lower:
            tool = "budget"
        elif "itinerary" in message_lower or "trip" in message_lower or "plan" in message_lower or "visit" in message_lower:
            tool = "itinerary"
        elif "pack" in message_lower or "clothing" in message_lower or "gear" in message_lower:
            tool = "packing"
            
        # 2. Extract destination (simple heuristic)
        destination = "Paris"
        match = re.search(r'(?:to|in|for)\s+([A-Z][a-z]+(?:\s+[A-Z][a-z]+)*)', message)
        if match:
            destination = match.group(1)
        else:
            match_any = re.search(r'(?:to|in|for)\s+([a-zA-Z]+)', message)
            if match_any:
                destination = match_any.group(1).capitalize()
                
        # 3. Extract days
        days = 5
        days_match = re.search(r'(\d+)\s*day', message_lower)
        if days_match:
            days = int(days_match.group(1))
            
        return {
            "tool": tool,
            "arguments": {
                "destination": destination,
                "days": days
            }
        }