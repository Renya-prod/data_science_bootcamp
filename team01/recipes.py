#!/usr/bin/env python3

import requests
import joblib
import pandas as pd
import numpy as np

class RecipePredictor:
    """Класс для предсказания рейтинга блюда на основе ингредиентов"""
    
    def __init__(self, model_path):
        self.model = joblib.load(model_path)
        self.ingredient_list = self.model.feature_names_in_ 

    def predict_rating(self, ingredients):
        """Предсказывает рейтинг блюда"""
        ingredient_vector = np.zeros(len(self.ingredient_list))
        for i, ingredient in enumerate(self.ingredient_list):
            if ingredient in ingredients:
                ingredient_vector[i] = 1

        input_df = pd.DataFrame([ingredient_vector], columns=self.ingredient_list)

        rating = self.model.predict(input_df)[0]
        return round(rating, 2)


class NutrientAnalyzer:
    """Класс для анализа питательной ценности ингредиентов с учетом суточных норм"""

    RDIs = {
        "vitamin A": 900, "vitamin C": 90, "calcium": 1300, "iron": 18, "vitamin D": 20,
        "vitamin E": 15, "vitamin K": 120, "potassium": 4700, "magnesium": 420, "zinc": 11
    }
    
    DRVs = {
        "fat": 178, "saturated fat": 120, "cholesterol": 300, "carbohydrates": 1275,
        "fiber": 128, "protein": 150, "sodium": 2300, "added sugars": 150
    }

    def __init__(self, nutrient_data_path):
        self.nutrient_data = pd.read_csv(nutrient_data_path)

    def analyze_nutrients(self, ingredients):
        """Возвращает нутриенты в % от суточной нормы"""
        selected_nutrients = self.nutrient_data[self.nutrient_data['ingredient'].isin(ingredients)]
        if selected_nutrients.empty:
            return "Нет информации о питательной ценности"

        result = []
        for _, row in selected_nutrients.iterrows():
            nutrients = {}
            for nutrient in self.RDIs.keys():
                if nutrient in row:
                    percent = (row[nutrient] / self.RDIs[nutrient]) * 100
                    nutrients[nutrient] = f"{percent:.1f}%"

            for nutrient in self.DRVs.keys():
                if nutrient in row:
                    percent = (row[nutrient] / self.DRVs[nutrient]) * 100
                    nutrients[nutrient] = f"{percent:.1f}%"

            result.append({"ingredient": row["ingredient"], **nutrients})
        
        return result

import requests
import pandas as pd

class RecipeRecommender:
    """Класс для поиска похожих рецептов через FDC API"""
    
    API_KEY = "LfLOwuhRE2bJcNaaZVPyGYcN3kCIeHy2pG41ayxS"

    def __init__(self):
        self.base_url = "https://api.nal.usda.gov/fdc/v1/foods/search"

    def fetch_recipes_from_api(self, query):
        """Запрашивает рецепты из API USDA по названию ингредиента"""
        params = {
            "api_key": self.API_KEY,
            "query": query,
            "pageSize": 10
        }
        response = requests.get(self.base_url, params=params)
        if response.status_code == 200:
            return response.json().get("foods", [])
        return []

    def find_similar_recipes(self, ingredients, top_n=3):
        """Ищет похожие рецепты по ингредиентам с USDA API"""
        similar_recipes = []
        
        for ingredient in ingredients:
            recipes = self.fetch_recipes_from_api(ingredient)
            for recipe in recipes:
                similar_recipes.append({
                    "title": recipe.get("description", "Unknown Recipe"),
                    "rating": recipe.get("foodNutrients", [{}])[0].get("value", "-"),
                    "url": f"https://fdc.nal.usda.gov/fdc-app.html#/food-details/{recipe.get('fdcId', '')}/nutrients"
                })

        if not similar_recipes:
            return [{"title": "No matching recipes", "rating": "-", "url": "-"}]

        df_recipes = pd.DataFrame(similar_recipes).drop_duplicates().sort_values(by="rating", ascending=False)
        return df_recipes.head(top_n).to_dict(orient="records")

class MenuGenerator:
    """Класс для составления дневного меню"""
    
    def __init__(self, recipes_path, nutrient_data_path):
        self.recipes = pd.read_csv(recipes_path)
        self.nutrient_data = pd.read_csv(nutrient_data_path)
    
    def generate_daily_menu(self):
        """Генерирует меню на день (завтрак, обед, ужин)"""
        
        daily_limits = {"calories": 100, "protein": 100, "fat": 100, "sodium": 100}
        
        categories = ["breakfast", "lunch", "dinner"]
        menu = {}

        for category in categories:
            category_recipes = self.recipes[self.recipes['category'] == category]
            
            selected_recipe = None
            for _, recipe in category_recipes.iterrows():
                nutrients = self.nutrient_data[self.nutrient_data['ingredient'].isin(recipe['ingredients'].split(", "))]
                if nutrients.empty:
                    continue

                total_nutrients = nutrients[['protein', 'fat', 'sodium']].sum()

                if (total_nutrients.reindex(daily_limits.keys(), fill_value=0) <= pd.Series(daily_limits)).all():
                    selected_recipe = recipe
                    break
            
            if selected_recipe is not None:
                menu[category] = {
                    "title": selected_recipe["title"],
                    "rating": selected_recipe["rating"],
                    "ingredients": selected_recipe["ingredients"],
                    "url": selected_recipe["url"]
                }

        return menu
