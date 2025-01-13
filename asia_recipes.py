import random

class Asia():
    """
    This class contains 3 functions that include recipes from different regions of Asia. Each function returns a random recipe.
    """

    def East_Asia():

        chinese_dish = "Tomato and Egg"
        chinese_ingredients = ", ".join(["4 tomatoes", "1 scallion", "4 eggs", "3/4 tsp salt", "1/4 tsp white pepper", "1/2 tsp sesame oil", "1 tsp shaoxing wine", 
        "3 tbsp vegetable oil", "2 tsp sugar", "1/2 cup water"])
        chinese_instructions = """
        Step 1: Cut tomatoes into small wedges and chop scallions. 
        Step 2: Crack eggs into a bowl and season with ¼ teaspoon salt, ¼ teaspoon white pepper, ½ teaspoon sesame oil, and 1sp of shaoxing wine, beat eggs. 
        Step 3: Preheat wok and add 2 tbsp of oil and the eggs, scramble and then set aside. 
        Step 4: Add 1 tbsp of oil, add tomatoes and scallions, cook for 1 minute, then add 2 teaspoons sugar, ½ teaspoon salt, and ¼ cup water. 
        Step 5: Mix egg and tomatoes together, cover wok, and let cook for 1-2 minutes. 
        Step 6: Uncover wok and stir until liking, serve."""
        chinese_recipe = {"name": chinese_dish, "ingredients": chinese_ingredients, "instructions": chinese_instructions}

        korean_dish = "Kimchi Fried Rice"
        korean_ingredients = ", ".join(["8 1/2 inch slices of bacon", "2 cups of chopped kimchi", "1/3 cup kimchi juice", "4 cups rice", "3 tbsp gochujang",
        "2 tbsp sesame oil", "4 scallions"])
        korean_instructions = """
        Step 1: Add bacon to pan and cook until crispy.
        Step 2: Add kimchi to cook for 1 minute, then add rice and mix together.
        Step 3: Add kimchi juice and gochujang and stir, add water if rice is dry.
        Step 4: Cook for about 5 minutes and serve.
        """
        korean_recipe = {"name": korean_dish, "ingredients": korean_ingredients, "instructions": korean_instructions}

        japanese_dish = "Miso Soup"
        japanese_ingredients = ", ".join(["4 cups water", "1 piece of dried kelp", "6 oz. of tofu", "1 tsp dried wakame", "3 tbsp miso paste", "1/4 cup scallions"])
        japanese_instructions = """
        Step 1: Heat a large pot of water, add dried kelp and let cook until simmering.
        Step 2: Remove kelp and let sit for 5 minutes.
        Step 3: Cut and add tofu and wakame into pot and stir.
        Step 4: Add kelp and miso paste into bowl and mix, then add into pot.
        Step 5: Stir until liking, then garnish with scallions and serve.
        """
        japanese_recipe = {"name": japanese_dish, "ingredients": japanese_ingredients, "instructions": japanese_instructions}


        random_pick = [chinese_recipe, korean_recipe, japanese_recipe]
        select_recipe = random.choice(random_pick)
        if select_recipe == chinese_recipe:
            print("Here is a Chinese dish.")
            return "\n".join([f"Name: {chinese_recipe['name']}", f"Ingredients: {chinese_recipe['ingredients']}", f"Instructions: {chinese_recipe['instructions']}"])
        
        elif select_recipe == korean_recipe:
            print("Here is a Korean dish.")
            return "\n".join([f"Name: {korean_recipe['name']}", f"Ingredients: {korean_recipe['ingredients']}", f"Instructions: {korean_recipe['instructions']}"])
        
        else:
            print("Here is a Japanese dish.")
            return "\n".join([f"Name: {japanese_recipe['name']}", f"Ingredients: {japanese_recipe['ingredients']}", f"Instructions: {japanese_recipe['instructions']}"])


    def South_Asia():
        indian_dish = "Jeera Aloo"
        indian_ingredients = ", ".join(["4 potatoes", "1tbs cumin seeds", "2 tbsp oil", "1/2 tsp tumeric"])
        indian_instructions = """
        Step 1: Heat oil in pan.
        Step 2: Add cumin seeds, diced potatoes, tumeric, and salt, then mix together.
        Step 3: Cover pan and let cook until potatoes are tender, serve.
        """
        indian_recipe = {"name": indian_dish, "ingredients": indian_ingredients, "instructions": indian_instructions}

        pakistani_dish = "Chicken Karahi"
        pakistani_ingredients = ", ".join(["Whole chicken", "3 tomatoes", "1 tbsp ginger", "2 green chilies", "2 tbsp karahi masala"])
        pakistani_instructions = """
        Step 1: Heat pan and add chopped chicken, tomatoes, and ginger into pan.
        Step 2: Add masala into pan and stir ingredients together.
        Step 3: Cover pan and let it simmer slowly until chicken is cooked.
        Step 4: Garnish with green chilies and serve with rice.
        """
        pakistani_recipe = {"name": pakistani_dish, "ingredients": pakistani_ingredients, "instructions": pakistani_instructions}

        nepali_dish = "Gundruk"
        nepali_ingredients = ", ".join(["1 cup of gundruk", "2 tomatoes", "1 onion", "2 green chilies", "2 tbsp, mustard oil"])
        nepali_instructions = """
        Step 1: Mix gundruk with chopped tomatoes, onion, and green chilies in a bowl.
        Step 2: Heat mustard oil in a pan and mix into the bowl.
        Step 3: Serve.
        """
        nepali_recipe = {"name": nepali_dish, "ingredients": nepali_ingredients, "instructions": nepali_instructions}


        random_pick = [indian_recipe, pakistani_recipe, nepali_recipe]
        select_recipe = random.choice(random_pick)
        if select_recipe == indian_recipe:
            print("Here is a Indian dish.")
            return "\n".join([f"Name: {indian_recipe['name']}", f"Ingredients: {indian_recipe['ingredients']}", f"Instructions: {indian_recipe['instructions']}"])
        
        elif select_recipe == pakistani_recipe:
            print("Here is a Pakistani dish.")
            return "\n".join([f"Name: {pakistani_recipe['name']}", f"Ingredients: {pakistani_recipe['ingredients']}", f"Instructions: {pakistani_recipe['instructions']}"])
        
        else:
            print("Here is a Nepali dish.")
            return "\n".join([f"Name: {nepali_recipe['name']}", f"Ingredients: {nepali_recipe['ingredients']}", f"Instructions: {nepali_recipe['instructions']}"])
          


    def Southeast_Asia():
        vietnamese_dish = "Pho"
        vietnamese_ingredients = ", ".join(["rice noodles", "beef slices", "1 onion", "1 ginger", "4 cups beef broth", "2 tbsp fish sauce", "1 tbsp soy sauce", "1 tbsp sugar",
        "herbs (cilantro and basil)", "bean sprouts and lime"])
        vietnamese_instructions = """
        Step 1: Cooke rice noodles and set aside.
        Step 2: In a pot, add the beef broth, sliced onion, and ginger and boil for 15 minutes.
        Step 3: Briefly cook beef slices and set aside.
        Step 4: Add fish sauce, soy sauce, and sugar into the broth and taste until liking.
        Step 5: In a bowl, add rice noodles, broth, and beef slices.
        Step 6: Garnish with herbs, bean sprouts, and lime slices.
        Step 7: Serve.
        """
        vietnamese_recipe = {"name": vietnamese_dish, "ingredients": vietnamese_ingredients, "instructions": vietnamese_instructions}

        filipino_dish = "Adobo"
        filipino_ingredients = ", ".join(["1 chicken", "1 cup soy sauce", "1 cup vinegar", "4 cloves garlic", "1 teaspoon peppercorns"])
        filipino_instructions = """
        Step 1: Combine the chicken, soy sauce, vinegar, garlic, and peppercorns into a pot.
        Step 2: Marinate the chicken for an hour.
        Step 3: Boil the mixture, once boiling, reduce heat to let cook for 30 minutes.
        Step 4: Occasionally stir and once ready, serve over rice.
        """
        filipino_recipe = {"name": filipino_dish, "ingredients": filipino_ingredients, "instructions": filipino_instructions}

        thai_dish = "Pad Thai"
        thai_ingredients = ", ".join(["rice noodles", "shrimp", "2 eggs", "1 cup bean sprouts", "3 tbsp soy sauce"])
        thai_instructions = """
        Step 1: Cook rice noodles and set aside.
        Step 2: Stir fry shrimp in wok until cooked.
        Step 3: Beat and scramble eggs with shrimp.
        Step 4: Add the cooked noodles to the wok, along with bean sprouts and soy sauce, and mix together.
        Step 5: (Optional) Add peanuts, lime slices, and cilantro as garnish.
        """
        thai_recipe = {"name": thai_dish, "ingredients": thai_ingredients, "instructions": thai_instructions}


        random_pick = [vietnamese_recipe, filipino_recipe, thai_recipe]
        select_recipe = random.choice(random_pick)
        if select_recipe == vietnamese_recipe:
            print("Here is a Vietnamese dish.")
            return "\n".join([f"Name: {vietnamese_recipe['name']}", f"Ingredients: {vietnamese_recipe['ingredients']}", f"Instructions: {vietnamese_recipe['instructions']}"])
        
        elif select_recipe == filipino_recipe:
            print("Here is a Filipino dish.")
            return "\n".join([f"Name: {filipino_recipe['name']}", f"Ingredients: {filipino_recipe['ingredients']}", f"Instructions: {filipino_recipe['instructions']}"])
        
        else:
            print("Here is a Thai dish.")
            return "\n".join([f"Name: {thai_recipe['name']}", f"Ingredients: {thai_recipe['ingredients']}", f"Instructions: {thai_recipe['instructions']}"])
