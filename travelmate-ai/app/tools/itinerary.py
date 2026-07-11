class ItineraryTool:

    @staticmethod
    def create(destination: str, days: int):

        itinerary = []

        for day in range(1, days + 1):
            itinerary.append({
                "day": day,
                "title": f"Explore {destination}",
                "activities": [
                    "Breakfast",
                    "Sightseeing",
                    "Lunch",
                    "Local Market",
                    "Dinner"
                ]
            })

        return itinerary