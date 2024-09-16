"""Aufgabe 8 LU02"""
# Dein Code kommt hier hin

import json


def load_recipe(json_string):
    return json.loads(json_string)


def adjust_recipe(recipe_data, new_servings):
    original_servings = recipe_data['servings']
    adjustment_factor = new_servings / original_servings

    adjusted_ingredients = {
        ingredient: quantity * adjustment_factor
        for ingredient, quantity in recipe_data['ingredients'].items()
    }

    adjusted_recipe_data = {
        'title': recipe_data['title'],
        'ingredients': adjusted_ingredients,
        'servings': new_servings
    }

    return adjusted_recipe_data

if __name__ == '__main__':
    # Beispiel für die Datenstruktur eines Rezepts
    recipe_json = '{"title": "Spaghetti Bolognese", "ingredients": {"Spaghetti": 400, "Tomato Sauce": 300,' \
                  ' "Minced Meat": 500}, "servings": 4}'
    # Dein Code kommt hier hin

    original_recipe = load_recipe(recipe_json)
    print('Originales Rezept:')
    print(json.dumps(original_recipe, indent=4))

    adjusted_recipe_2 = adjust_recipe(original_recipe, 2)
    print('\nAngepasstes Rezept für 2 Personen:')
    print(json.dumps(adjusted_recipe_2, indent=4))

    adjusted_recipe_6 = adjust_recipe(original_recipe, 6)
    print('\nAngepasstes Rezept für 6 Personen:')
    print(json.dumps(adjusted_recipe_6, indent=4))