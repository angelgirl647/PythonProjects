# A list can store a sequence of objects in a certain order such that you can index into the list, or iterate over the list.
# List is a mutable type meaning that lists can be modified after they have been created.

# A dictionary is a key-value store. It is not ordered and it requires that the keys are hashable. It is fast for lookups by key.

# recipe for spicy lemon garlic shrimp

# this is a list
ingredients=["shrimp", "butter", "parsley leaves", "kosher salt", "red pepper","garlic","lemon","crusty bread"]
# this is a dictionary so when you call shrimp, you get the number 2 as the amt you need to buy. shrimp=key and value=2
amtOfIngred={"shrimp":2,"butter":2}

# list to hold every step in the recipe
instructions=["1.Preheat the oven to 375 degrees F. Rinse the shrimp to separate, and then arrange in a single layer on a baking sheet",
"2.To the bowl of a food processor, add the butter, parsley, salt, red pepper, garlic and lemon juice. Pulse until combined. Sprinkle the cold butter crumbles over the shrimp",
"3.Bake until the shrimp is opaque and the butter is hot and bubbly.",
"4.Serve with hot crusty bread. Peel and eat the shrimp, and then encourage guests to dip the bread into the butter in the bottom of the pan."]

# dictionary that holds both lists
recipe={"ingredients":ingredients, "instructions":instructions}

# prints all ingred by calling the ingred list in the recipe dictionary
# print(recipe["ingredients"])
# print(recipe["instructions"][0])
# for item in range(4):
#     print(instructions[item])

# print(amtOfIngred["shrimp"])




userInput=input("What ingredients do you have?")
if userInput in ingredients:
    print("Try spicy lemon garlic chicken")
    yesOrNo=input("Want the recipe?")
    if yesOrNo == "yes"
        print(recipe)
    else:
        print("cool")

else:
    print("Sorry, no recipes available right now.Try again")
