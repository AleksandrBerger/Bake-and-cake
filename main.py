import sys


def cakes(recipe, ingredients):
    number_of_cakes = sys.maxsize
    keys = list(recipe.keys())
    for i in keys:
        if ingredients.get(i, 0) // recipe.get(i) < number_of_cakes:
            number_of_cakes = ingredients.get(i, 0) // recipe.get(i)
    print(number_of_cakes)


cakes({"apples": 3, "flour": 300, "sugar": 150, "milk": 100, "oil": 100},
      {"sugar": 500, "flour": 2000, "milk": 2000})
