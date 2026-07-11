class BudgetTool:

    @staticmethod
    def estimate(days: int, people: int = 1):

        hotel = 2500 * days * people
        food = 800 * days * people
        transport = 700 * days
        sightseeing = 1000 * days

        total = hotel + food + transport + sightseeing

        return {
            "hotel": hotel,
            "food": food,
            "transport": transport,
            "sightseeing": sightseeing,
            "total": total
        }