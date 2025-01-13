import random

class Europe():
    """
    This class contains 3 functions that include recipes from different regions of Europe. Each function returns a random recipe.
    """

    def eastern_europe():
        polish_dish = "Pierogi"
        polish_ingredients = ", ".join(["2 cups all-purpose flour", "1/2 cup water", "1 egg", "1/2 tsp salt", "1 cup mashed potatoes (cheese, onions, and meat)"])
        polish_instructions = """
        Step 1: Mix flour, water, egg, and salt to form a dough, then roll the dough and cut into circles.
        Step 2: Place a spoonful of mashed potato filling on each circle, fold in half, and press edges to seal.
        Step 3: Boil pierogi until they float, then fry in butter until golden.
        Step 4: Serve.
        """
        polish_recipe = {"name": polish_dish, "ingredients": polish_ingredients, "instructions": polish_instructions}

        ukranian_dish = "Borscht"
        ukranian_ingredients = ", ".join(["3 beets", "1 onion", "2 carrots", "4 cups of vegetable broth", "sour cream"])
        ukranian_instructions = """
        Step 1: Grate beets and carrots, chop onions.
        Step 2: Saute onions, then add beets and carrots.
        Step 3: Pour broth in and cook vegetables until tender.
        Step 4: Serve with a scoop of sour cream on top.
        """
        ukranian_recipe = {"name": ukranian_dish, "ingredients": ukranian_ingredients, "instructions": ukranian_instructions}

        hungarian_dish = "Chicken Paprikash"
        hungarian_ingredients = ", ".join(["1 chicken", "1 onion", "2 tbsp hungarian paprika", "1 cup chicken broth", "sour cream"])
        hungarian_instructions = """
        Step 1: Saute chopped onion and add chopped chicken to cook until brown.
        Step 2: Add the paprika, then pour chicken broth over, stir and cover.
        Step 3: Once chicken is cooked, stir in sour cream to make a creamy texture.
        Step 4: Once chicken in nicely covered with the sauce, serve.
        """
        hungarian_recipe = {"name": hungarian_dish, "ingredients": hungarian_ingredients, "instructions": hungarian_instructions}


        random_pick = [polish_recipe, ukranian_recipe, hungarian_recipe]
        select_recipe = random.choice(random_pick)
        if select_recipe == polish_recipe:
            print("Here is a Polish dish.")
            return "\n".join([f"Name: {polish_recipe['name']}", f"Ingredients: {polish_recipe['ingredients']}", f"Instructions: {polish_recipe['instructions']}"])
        
        elif select_recipe == ukranian_recipe:
            print("Here is a Ukranian dish.")
            return "\n".join([f"Name: {ukranian_recipe['name']}", f"Ingredients: {ukranian_recipe['ingredients']}", f"Instructions: {ukranian_recipe['instructions']}"])
        
        else:
            print("Here is a Hungarian dish.")
            return "\n".join([f"Name: {hungarian_recipe['name']}", f"Ingredients: {hungarian_recipe['ingredients']}", f"Instructions: {hungarian_recipe['instructions']}"])


    def western_europe():
        french_dish = "Coq au Vin"
        french_ingredients = ", ".join(["1 chicken", "bacon", "red wine", "2 cups chicken broth", "1 onion", "2 carrots", "3 cloves garlic", "2 tbsp flour", "3 tbsp butter"])
        french_instructions = """
        Step 1: Season chicken with salt and pepper, then brown in a pan with butter and set chicken aside.
        Step 2: Cook bacon in pan until crispy and mix in chopped onion, carrots, and garlic.
        Step 3: Add wine and chicken broth and stir to make the sauce.
        Step 4: Return chicken and bacon to the pan, cover, and simmer until chicken is cooked through.
        Step 5: Serve.
        """
        french_recipe = {"name": french_dish, "ingredients": french_ingredients, "instructions": french_instructions}

        british_dish = "Shepherd's Pie"
        british_ingredients = ", ".join(["ground beef", "1 onion", "2 cups of mixed vegetables", "4 cups of mached potatoes"])
        british_instructions = """
        Step 1: Add ground beef into a pan to brown, then add chopped onions with beef and let cook.
        Step 2: Add mixed vegetables and mix ingredients together.
        Step 3: Place mixture into a baking dish and spread the mashed potatoes on top.
        Step 4: Bake in oven until top is golden brown at 400 degrees fahrenheit.
        Step 5: Once baked for individual liking, serve.
        """
        british_recipe = {"name": british_dish, "ingredients": british_ingredients, "instructions": british_instructions}

        spanish_dish = "Patatas Bravas"
        spanish_ingredients = ", ".join(["4 potatoes", "olive oil", "1 cup of tomato sauce", "1 tsp paprika"])
        spanish_instructions = """
        Step 1: Drizzle olive oil onto a pan and add sliced potatoes, cook until golden brown.
        Step 2: Add tomato sauce and paprika into another pan and let simmer for a few minutes.
        Step 3: Pour tomato sauce over cooked potatoes and serve.
        """
        spanish_recipe = {"name": spanish_dish, "ingredients": spanish_ingredients, "instructions": spanish_instructions}
        

        random_pick = [french_recipe, british_recipe, spanish_recipe]
        select_recipe = random.choice(random_pick)
        if select_recipe == french_recipe:
            print("Here is a French dish.")
            return "\n".join([f"Name: {french_recipe['name']}", f"Ingredients: {french_recipe['ingredients']}", f"Instructions: {french_recipe['instructions']}"])
        
        elif select_recipe == british_recipe:
            print("Here is a British dish.")
            return "\n".join([f"Name: {british_recipe['name']}", f"Ingredients: {british_recipe['ingredients']}", f"Instructions: {british_recipe['instructions']}"])
        
        else:
            print("Here is a Spanish dish.")
            return "\n".join([f"Name: {spanish_recipe['name']}", f"Ingredients: {spanish_recipe['ingredients']}", f"Instructions: {spanish_recipe['instructions']}"])
        
    
    def northern_europe():
        swedish_dish = "Gravlax"
        swedish_ingredients = ", ".join(["1 salmon filet", "1 cup salt", "1 cup sugar", "dill", "black pepper"])
        swedish_instructions = """
        Step 1: Mix salt and sugar in a bowl.
        Step 2: Place salmon onto a tray and rub salt and sugar mixture on salmon.
        Step 3: Sprinkle dill and pepper on salmon.
        Step 4: Refrigerate salmon for 2-3 days and once the salmon is cured, serve with bread and mustard sauce.
        """
        swedish_recipe = {"name": swedish_dish, "ingredients": swedish_ingredients, "instructions": swedish_instructions}

        irish_dish = "Colcannon"
        irish_ingredients = ", ".join(["4 potatoes", "1/2 head of cabbage", "1/2 cup of butter", "1/2 cup of milk", "salt and pepper"])
        irish_instructions = """
        Step 1: Boil chopped potatoes, then set aside.
        Step 2: Then boil shredded cabbage, set aside afterwards.
        Step 3: Mash the potatoes together while mixing in butter until melted, gradually add milk until it has a creamy consistency.
        Step 4: Stir in cabbage and add aslt and pepper until liking, then serve.
        """
        irish_recipe = {"name": irish_dish, "ingredients": irish_ingredients, "instructions": irish_instructions}

        norwegian_dish = "Raspeballer"
        norwegian_ingredients = ", ".join(["4 potatoes", "1 cup flour", "1 tsp salt", "butter"])
        norwegian_instructions = """
        Step 1: Grate and peel potatoes into a bowl.
        Step 2: Mix in flour and salt for dough.
        Step 3: Hand wrap dough and potatoes together to form a ball.
        Step 4: Boil the potato balls in salted water until they float.
        Step 5: Serve with melted butter, can be served with salted meat or bacon (Optional).
        """
        norwegian_recipe = {"name": norwegian_dish, "ingredients": norwegian_ingredients, "instructions": norwegian_instructions}

        random_pick = [swedish_recipe, irish_recipe, norwegian_recipe]
        select_recipe = random.choice(random_pick)
        if select_recipe == swedish_recipe:
            print("Here is a Swedish dish.")
            return "\n".join([f"Name: {swedish_recipe['name']}", f"Ingredients: {swedish_recipe['ingredients']}", f"Instructions: {swedish_recipe['instructions']}"])
        
        elif select_recipe == irish_recipe:
            print("Here is a Irish dish.")
            return "\n".join([f"Name: {irish_recipe['name']}", f"Ingredients: {irish_recipe['ingredients']}", f"Instructions: {irish_recipe['instructions']}"])
        
        else:
            print("Here is a Norwegian dish.")
            return "\n".join([f"Name: {norwegian_recipe['name']}", f"Ingredients: {norwegian_recipe['ingredients']}", f"Instructions: {norwegian_recipe['instructions']}"])