from world_of_food import choose_continent as cc
from create_recipe import Recipe

def test_choose_continent():
   assert cc("asia") == "asia"
   assert cc("europe") == "europe"
   assert cc("africa") == "africa"

def test_init_():
    name = "Hot Dog"
    ingredients = ["hot dog", "bread", "condiment"]
    instructions = ["cook hot dog", "place hot dog on bread", "put condiment on", "serve"]
    total_time = "10 minutes"
    rating = "5"
    test_recipe = Recipe(name, ingredients, instructions, total_time, rating)

    assert test_recipe.name == "Hot Dog"
    assert test_recipe.ingredients == ["hot dog", "bread", "condiment"]
    assert test_recipe.instructions == ["cook hot dog", "place hot dog on bread", "put condiment on", "serve"]
    assert test_recipe.total_time == "10 minutes"
    assert test_recipe.rating == "5"
    assert test_recipe == test_recipe

def test_recipe_elements():
    test_recipe = Recipe("", [], [], "", "")
    test_recipe.name = "Test Recipe"
    test_recipe.ingredients = ["Ingredient 1", "Ingredient 2"]
    test_recipe.instructions = ["Step 1", "Step 2"]
    test_recipe.total_time = "10 minutes"
    test_recipe.rating = "5"
    #print(test_recipe)

    assert test_recipe.name == "Test Recipe"
    assert test_recipe.ingredients == ["Ingredient 1", "Ingredient 2"]
    assert test_recipe.instructions == ["Step 1", "Step 2"]
    assert test_recipe.total_time == "10 minutes"
    assert test_recipe.rating == "5"

def test_display_recipe():
    test_recipe = Recipe("", [], [], "", "")
    test_recipe.name = "Test Recipe"
    test_recipe.ingredients = ["Ingredient 1", "Ingredient 2"]
    test_recipe.instructions = ["Step 1", "Step 2"]
    test_recipe.total_time = "10 minutes"
    test_recipe.rating = "5"

    test_recipe.display_recipe()
 
if __name__ == "__main__":
    test_choose_continent()
    test_init_()
    test_recipe_elements()
    test_display_recipe()