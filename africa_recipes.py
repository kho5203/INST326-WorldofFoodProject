import random

class Africa():
    """
    This class contains 3 functions that include recipes from different regions of Africa. Each function returns a random recipe.
    """

    def eastern_africa():
        ethiopian_dish = "Doro Wat"
        ethiopian_ingredients = ", ".join(["1 chicken", "2 onions", "3 cloves of garlic", "1 tbsp ginger", "berbere spice", "2 tbsp tomato paste"])
        ethiopian_instructions = """
        Step 1: Saute chopped onions, then add garlic and ginger in large pot.
        Step 2: Stir in tomato paste and berbere spice.
        Step 3: Add chicken pieces into pot, and let cook until 10 minutes.
        Step 4: Pour water to cover chicken, let cook until sauce has thickened.
        """
        ethiopian_recipe = {"name": ethiopian_dish, "ingredients": ethiopian_ingredients, "instructions": ethiopian_instructions}

        kenyan_dish = "Nyama Choma"
        kenyan_ingredients = ", ".join(["slices of beef or goat meat", "2 tbsp vegetable oil", "1 tbsp paprika", "1 tsp cayenne pepper", "1 lemon"])
        kenyan_instructions = """
        Step 1: Combine meat with salt, vegetable oil, paprika, cayenne pepper, and the juice of one lemon.
        Step 2: Marinate the meat for 30 minutes.
        Step 3: Put marinated meat onto skewers and put on the grill.
        Step 4: Put more marinade on meat as you grill the meat.
        Step 5: Serve.
        """
        kenyan_recipe = {"name": kenyan_dish, "ingredients": kenyan_ingredients, "instructions": kenyan_instructions}

        somalian_dish = "Suugo Suqaar"
        somalian_ingredients = ", ".join(["sliced beef or chicken", "2 tbsp vegetable oil", "2 onions", "3 tomatoes", "2 tbsp tomato paste", "1 tsp cumin", "1 tsp coriander"])
        somalian_instructions = """
        Step 1: Heat vegetable oil and sauté the chopped onions until golden brown in a pan.
        Step 2: Add sliced meat to the pan and cook until browned.
        Step 3: Stir in the diced tomatoes, tomato paste, cumin, coriander, salt, and pepper and let cook until tomatoes break down and forms a thick sauce.
        Step 4: Let simmer for a few minutes and serve.
        """
        somalian_recipe = {"name": somalian_dish, "ingredients": somalian_ingredients, "instructions": somalian_instructions}

        random_pick = [ethiopian_recipe, kenyan_recipe, somalian_recipe]
        select_recipe = random.choice(random_pick)
        if select_recipe == ethiopian_recipe:
            print("Here is a Ethiopian dish.")
            return "\n".join([f"Name: {ethiopian_recipe['name']}", f"Ingredients: {ethiopian_recipe['ingredients']}", f"Instructions: {ethiopian_recipe['instructions']}"])
        
        elif select_recipe == kenyan_recipe:
            print("Here is a Kenyan dish.")
            return "\n".join([f"Name: {kenyan_recipe['name']}", f"Ingredients: {kenyan_recipe['ingredients']}", f"Instructions: {kenyan_recipe['instructions']}"])
        
        else:
            print("Here is a Somalian dish.")
            return "\n".join([f"Name: {somalian_recipe['name']}", f"Ingredients: {somalian_recipe['ingredients']}", f"Instructions: {somalian_recipe['instructions']}"])

        

    def western_africa():
        nigerian_dish = "Jollof Rice"
        nigerian_ingredients = ", ".join(["2 cups long grain rice", "1/4 cup vegetable oil", "1 onion", "2 red bell peppers", "3 tomatoes", "2 tsp tomato paste", 
        "2 tsp cayenne pepper", "1 tsp thyme", "2 bay leaves", "2 1/2 cup chicken broth"])
        nigerian_instructions = """
        Step 1: Heat vegetable oil and add chopped onions into a large pot.
        Step 2: Put tomatoes and bell peppers into blender and add to pot, then stir in tomato paste, cayenne, thyme, and bay leaves.
        Step 3: Add rice and chicken broth into the pot and mix well.
        Step 4: Let mixture boil and cover pot, once rice is cooked, serve.
        """
        nigerian_recipe = {"name": nigerian_dish, "ingredients": nigerian_ingredients, "instructions": nigerian_instructions}

        ghanian_dish = "Ghanian Kelewele"
        ghanian_ingredients = ", ".join(["4 plantains", "2 tbsp ginger", "1 tsp cayenne pepper", "1 tsp paprika"])
        ghanian_instructions = """
        Step 1: Peel and cut plantains into chunks.
        Step 2: Grate ginger and combine cayenne, paprika, salt, and mix in a bowl.
        Step 3: Cover the plantains with the spice mix.
        Step 4: In a pan, add vegetable oil and cook plantains until golden brown and crispy.
        """
        ghanian_recipe = {"name": ghanian_dish, "ingredients": ghanian_ingredients, "instructions": ghanian_instructions}

        senegalese_dish = "Thieboudienne "
        senegalese_ingredients = ", ".join(["1 fish (red snapper)", "2 cups rice", "1 eggplant", "2 carrots", "1 onion", "2 tomatoes", "1/2 cup tomato paste", 
        "1/4 cooking oil", "2 cloves garlic", "1 tbsp ground pepper"])
        senegalese_instructions = """
        Step 1: Clean and season fish with salt, then set aside.
        Step 2: saute chopped oinions and minced garlic in a large pot.
        Step 3: Add diced tomatoes, tomato paste, ground pepper, sliced eggplant, sliced carrots, and stir well.
        Step 4: Place fish inside pot with the mixture and add water to cover ingredients and bring to boil.
        Step 5: Add rice to the pot and let cook until rice is cooked and fish is tender.
        """
        senegalese_recipe = {"name": senegalese_dish, "ingredients": senegalese_ingredients, "instructions": senegalese_instructions}


        random_pick = [nigerian_recipe, ghanian_recipe, senegalese_recipe]
        select_recipe = random.choice(random_pick)
        if select_recipe == nigerian_recipe:
            print("Here is a Nigerian dish.")
            return "\n".join([f"Name: {nigerian_recipe['name']}", f"Ingredients: {nigerian_recipe['ingredients']}", f"Instructions: {nigerian_recipe['instructions']}"])
        
        elif select_recipe == ghanian_recipe:
            print("Here is a Ghanian dish.")
            return "\n".join([f"Name: {ghanian_recipe['name']}", f"Ingredients: {ghanian_recipe['ingredients']}", f"Instructions: {ghanian_recipe['instructions']}"])
        
        else:
            print("Here is a Senegalese dish.")
            return "\n".join([f"Name: {senegalese_recipe['name']}", f"Ingredients: {senegalese_recipe['ingredients']}", f"Instructions: {senegalese_recipe['instructions']}"])



    def southern_africa():
        south_african_dish = "Bobotie"
        south_african_ingredients = ", ".join(["ground beef or lamb", "2 slices of white bread", "1 cup of milk", "1 onion", "2 tbsp curry powder", 
        "1 tbsp apricot jam", "2 tbsp vinegar", "2 eggs", "salt and pepper", "bay leaves"])
        south_african_instructions = """
        Step 1: Soak bread in milk and then mash the bread to form a mixture.
        Step 2: Saute chopped onions, add meat and curry powder and cook meat until brown.
        Step 3: Add bread mixture, apricot jam, vinegar, and season with salt and pepper.
        Step 4: Put the mixture into a baking dish and pour beaten eggs over the meat.
        Step 5: Add bay leaves on top, then bake for 30-40 minutes at 350 Farenheit.
        """
        south_african_recipe = {"name": south_african_dish, "ingredients": south_african_ingredients, "instructions": south_african_instructions}

        zambian_dish = "Nshima"
        zambian_ingredients = ", ".join(["2 cups maize meal", "water", "salt"])
        zambian_instructions = """
        Step 1: Boil a large pot of water and gradually stir in maize meal.
        Step 2: Cook maize meal until it forms a porridge and let steam for a few minutes.
        Step 3: Once cooked, take out the porridge and mold it into a round shape.
        Step 4: Serve with another Zambian dish like Ndiwo.
        """
        zambian_recipe = {"name": zambian_dish, "ingredients": zambian_ingredients, "instructions": zambian_instructions}

        rwandan_dish = "Rwandan Brochettes"
        rwandan_ingredients = ", ".join(["beef or goat meat", "1 onion", "2 cloves garlic", "1 tsp ginger", "2 tbsp vegetable oil", "salt and pepper"])
        rwandan_instructions = """
        Step 1: In a bowl, mix in chopped onion, minced garlic, vegetable oil, salt, and pepper to create a marinade.
        Step 2: Coat cut meat with the marinade and let marinate for 30 minutes.
        Step 3: Thread the marinated meat onto skewers, then grill, occasionally turning for even cooking.
        Step 4: Serve.
        """
        rwandan_recipe = {"name": rwandan_dish, "ingredients": rwandan_ingredients, "instructions": rwandan_instructions}

        
        random_pick = [south_african_recipe, zambian_recipe, rwandan_recipe]
        select_recipe = random.choice(random_pick)
        if select_recipe == south_african_recipe:
            print("Here is a South African dish.")
            return "\n".join([f"Name: {south_african_recipe['name']}", f"Ingredients: {south_african_recipe['ingredients']}", f"Instructions: {south_african_recipe['instructions']}"])
        
        elif select_recipe == zambian_recipe:
            print("Here is a Zambian dish.")
            return "\n".join([f"Name: {zambian_recipe['name']}", f"Ingredients: {zambian_recipe['ingredients']}", f"Instructions: {zambian_recipe['instructions']}"])
        
        else:
            print("Here is a Rwandan dish.")
            return "\n".join([f"Name: {rwandan_recipe['name']}", f"Ingredients: {rwandan_recipe['ingredients']}", f"Instructions: {rwandan_recipe['instructions']}"])