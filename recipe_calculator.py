# recipe_calculator.py

recipe = {"flour": 100, "sugar": 50, "eggs": 1}

def calculate_ingredients(servings):
    return {ingredient: amount * servings for ingredient, amount in recipe.items()}

# Sample usage
print("Ingredients for 3 servings:", calculate_ingredients(3))
