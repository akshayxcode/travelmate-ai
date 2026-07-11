from app.tools.budget import BudgetTool
from app.tools.itinerary import ItineraryTool
from app.tools.packing import PackingTool


class ToolManager:

    @staticmethod
    def execute(tool_name: str, **kwargs):

        if tool_name == "budget":
            return BudgetTool.estimate(
                days=kwargs.get("days", 3),
                people=kwargs.get("people", 1)
            )

        if tool_name == "itinerary":
            return ItineraryTool.create(
                destination=kwargs.get("destination", "Goa"),
                days=kwargs.get("days", 3)
            )

        if tool_name == "packing":
            return PackingTool.generate(
                destination=kwargs.get("destination", "Goa")
            )

        return None