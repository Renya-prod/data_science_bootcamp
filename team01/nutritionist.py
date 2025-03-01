#!/usr/bin/env python3

import sys
from recipes import RecipePredictor, NutrientAnalyzer, RecipeRecommender, MenuGenerator

MODEL_PATH = "data/recipe_rating_model.pkl"
NUTRIENT_DATA_PATH = "data/nutrients.csv"
RECIPES_PATH = "data/recipes.csv"

def categorize_rating(rating):
    """Определяет текстовый прогноз на основе рейтинга"""
    if rating < 2.5:
        return "You might find it tasty, but in our opinion, it is a bad idea to have a dish with that list of ingredients."
    elif rating < 4:
        return "It could be okay, but there are better combinations."
    else:
        return "This sounds like a delicious and nutritious meal!"

def format_nutrient_name(name):
    """Форматирует название нутриента (Vitamin A вместо vitamin a)"""
    return " ".join(word.capitalize() for word in name.split())

def main():
    if len(sys.argv) < 2:
        print("Usage: ./nutritionist.py <ingredients separated by commas>")
        return


    if sys.argv[1].lower() == "menu":
        menu_generator = MenuGenerator(RECIPES_PATH, NUTRIENT_DATA_PATH)
        daily_menu = menu_generator.generate_daily_menu()

        print("\n=== DAILY MENU ===\n")
        for category, meal in daily_menu.items():
            print(f"{category.upper()}\n---------------------")
            print(f"{meal['title']} (rating: {meal['rating']})")
            print(f"Ingredients: {meal['ingredients']}")
            print(f"URL: {meal['url']}\n")
        return

    input_ingredients = [i.strip().lower() for i in sys.argv[1].split(",")]

    # 1. Предсказание рейтинга
    predictor = RecipePredictor(MODEL_PATH)
    predicted_rating = predictor.predict_rating(input_ingredients)
    forecast_text = categorize_rating(predicted_rating)

    print("I. OUR FORECAST")
    print(f"{forecast_text}\n")

    # 2. Анализ питательной ценности
    analyzer = NutrientAnalyzer(NUTRIENT_DATA_PATH)
    nutrients_info = analyzer.analyze_nutrients(input_ingredients)

    print("II. NUTRITION FACTS")
    for nutrient in nutrients_info:
        print(f"{nutrient['ingredient'].capitalize()}:")
        for key, value in nutrient.items():
            if key != "ingredient":
                numeric_value = float(str(value).replace('%', '').strip())
                print(f"  {format_nutrient_name(key)} - {round(numeric_value)}% of Daily Value")
    print()

    # 3. Поиск похожих рецептов
    recommender = RecipeRecommender()
    similar_recipes = recommender.find_similar_recipes(input_ingredients)

    print("III. TOP-3 SIMILAR RECIPES:")
    if similar_recipes and similar_recipes[0]['title'] != "No matching recipes":
        for recipe in similar_recipes:
            print(f"- {recipe['title']}, rating: {recipe['rating']}, URL: {recipe['url']}")
    else:
        print("No matching recipes found.")


if __name__ == "__main__":
    main()
