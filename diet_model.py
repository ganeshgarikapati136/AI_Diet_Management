class DietConsultant:
    def __init__(self, name, age, weight, height, goal, preference="general", disease=None):
        self.name = name
        self.age = age
        self.weight = weight
        self.height = height
        self.goal = goal
        self.preference = preference
        self.disease = disease

    def calculate_bmi(self):
        return self.weight / (self.height ** 2)

    def suggest_diet(self):
        bmi = self.calculate_bmi()
        if self.disease:
            return self.disease_based_diet()
        elif bmi < 18.5:
            return self.format_diet(
                ["Whole grains", "Lean proteins"],
                ["Grilled fish", "Leafy greens"],
                ["Vegetable stew"],
                ["Nuts", "Dried fruits"]
            )
        elif bmi < 24.9:
            return self.format_diet(
                ["Greek yogurt", "Nuts", "Fruits"],
                ["Grilled chicken", "Broccoli"],
                ["Dairy-based meals", "Lean proteins"],
                ["Cheese", "Fruit"]
            )
        else:
            return self.format_diet(
                ["High-fiber cereal"],
                ["Lentil soup", "Whole grain bread"],
                ["Light vegetable soup", "Whole grains"],
                ["Raw veggies", "Hummus"]
            )

    def disease_based_diet(self):
        return {
            "cardiovascular": self.format_diet(
                ["Oats", "Berries"],
                ["Grilled salmon", "Quinoa"],
                ["Vegetable stir-fry"],
                ["Almonds"]
            ),
            "diabetes": self.format_diet(
                ["Whole grain toast", "Boiled egg"],
                ["Chicken salad", "Brown rice"],
                ["Steamed vegetables", "Lean protein"],
                ["Nuts", "Low-sugar yogurt"]
            ),
            "prostate": self.format_diet(
                ["Tomatoes", "Walnuts"],
                ["Grilled fish", "Leafy greens"],
                ["Vegetable stew"],
                ["Mixed nuts"]
            ),
            "lung": self.format_diet(
                ["Berry smoothie"],
                ["Lean meats", "Whole grains"],
                ["Vegetable soup"],
                ["Carrot sticks"]
            ),
            "liver": self.format_diet(
                ["Oatmeal", "Green tea"],
                ["Quinoa salad", "Grilled tofu"],
                ["Steamed fish", "Vegetables"],
                ["Fresh fruits"]
            ),
            "colorectal": self.format_diet(
                ["High-fiber cereal", "Banana"],
                ["Lentil soup", "Whole grain bread"],
                ["Grilled chicken", "Broccoli"],
                ["Greek yogurt"]
            ),
            "mental_health": self.format_diet(
                ["Salmon", "Avocado toast"],
                ["Spinach quinoa salad"],
                ["Brown rice", "Lean meat"],
                ["Dark chocolate", "Nuts"]
            ),
            "osteoporosis": self.format_diet(
                ["Milk", "Nuts"],
                ["Calcium-rich greens"],
                ["Dairy-based meals", "Lean proteins"],
                ["Cheese", "Fruit"]
            ),
            "sti": self.format_diet(
                ["Citrus fruits", "Garlic"],
                ["Protein-rich salad"],
                ["Vegetable curry", "Whole grains"],
                ["Green tea", "Berries"]
            )
        }.get(self.disease.lower(), self.format_diet([], [], [], []))

    def format_diet(self, breakfast, lunch, dinner, snacks):
        return {
            "Breakfast": breakfast,
            "Lunch": lunch,
            "Dinner": dinner,
            "Snacks": snacks
        }
