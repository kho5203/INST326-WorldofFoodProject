class Recipe():
    """
    This class is called recipe and is used when the user chooses "create" in the main file.
    """
    def __init__(self, name, ingredients, instructions, total_time, rating):
        """
        This function initializes variables.
        """
        self.name = name
        self.ingredients = ingredients
        self.instructions = instructions
        self.total_time = total_time
        self.rating = rating

    def recipe_elements(self):
        """
        In this function, each variable asks the user for an input based off of the prompt it gives.
        """
        self.name = input("Give a name for your recipe: ")
        self.ingredients = input("List your ingredients by using commas (Ex: bread, meat, etc.): ").strip(",").split(",")
        self.instructions = input("Write down your instructions by using periods (Ex: Cut onions. Place onions in pan.): ").strip(".").split(". ")
        self.total_time = input("Give an estimate on how long it will take to cook this dish: ")
        self.rating = input("Give this dish a rating from 1-5: ") 

    def display_recipe(self):
        """
        This function displays all of the elements of the recipe the user created.
        """
        ingredients_counter = 0
        instructions_counter = 0

        print(f"Name: {self.name}")
        print("Ingredients: ")
        for i in self.ingredients:
            ingredients_counter = ingredients_counter + 1
            print(f"\tIngredient {ingredients_counter}: {i.strip()}")
        print("Directions: ")
        for i in self.instructions:
            instructions_counter = instructions_counter + 1
            print(f"\tStep {instructions_counter}: {i}")
        print(f"Total Time: {self.total_time}")
        print(f"Rating: {self.rating}")

