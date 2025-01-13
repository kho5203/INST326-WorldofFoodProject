import asia_recipes
import europe_recipes
import africa_recipes
from create_recipe import Recipe

def choose_continent(user_continent):
        """
        This function makes sure the user inputs the valid continent after choosing "find".
        """
        valid_continents = ["asia", "europe", "africa"]

        continent = user_continent
        while True:
            if continent in valid_continents:
                print("You have chosen: ", continent)
                return continent
            
            else:
                  continent = input("Invalid input. Please choose either Asia, Europe, Africa: ").lower()

if __name__ == "__main__":
    
    """
    This script is called The World of Food and is a recipe book. It is able to show the user a diverse set of recipes based on the region they choose, guide the user in creating
    a recipe, and is able to display all of the recipes the user created.
    """

    asia = asia_recipes
    europe = europe_recipes
    africa = africa_recipes
    recipe_creation = 0
    saved_recipes = []
    print("Hello! Welcome to The World of Food!\nYou can either choose a recipe from our book or make your own!")
    
    while True:
        user = input("Do you want to lookup a recipe, create your own recipe, or view the amount of recipes you have created already? Please enter find, create, view or exit: ").lower()
        
        if user == "find":
            print("Lets find a recipe for you!")
            user_continent = input("Please choose a continent: Asia, Europe, Africa: ").lower()
            continent = choose_continent(user_continent)
            if continent == "asia":
                 print("Listed below are a couple Asian dishes you can try.")
                 print(asia.Asia.East_Asia())
                 print(asia.Asia.South_Asia())
                 print(asia.Asia.Southeast_Asia())
            
            elif continent == "europe":
                 print("Listed below are a couple European dishes you can try.")
                 print(europe.Europe.eastern_europe())
                 print(europe.Europe.western_europe())
                 print(europe.Europe.northern_europe())

            elif continent == "africa":
                 print("Listed below are a couple African dishes you can try.")
                 print(africa.Africa.eastern_africa())
                 print(africa.Africa.western_africa())
                 print(africa.Africa.southern_africa())

        elif user == "create":
            recipe_creation = recipe_creation + 1
            new_recipe = Recipe("", [], [], "", "")
            print("Lets help you create a recipe!")
            new_recipe.recipe_elements()
            print("Here is the recipe you just created.")
            new_recipe.display_recipe()
            saved_recipes.append(new_recipe)

        elif user == "view":
             print(f"You have created {recipe_creation} recipes so far.")
             for i in range(len(saved_recipes)):
                  print(f"\nRecipe {i + 1}")
                  saved_recipes[i].display_recipe()

        elif user == "exit":
            print("You have exited The World of Food.")
            break

        else:
            print("Invalid input, please enter either find, create, or exit.")