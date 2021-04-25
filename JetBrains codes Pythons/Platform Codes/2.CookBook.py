'''https://hyperskill.org/learn/step/6520#solutions

Any recipe starts with a list of ingredients. Below is an extract from a cookbook with the ingredients for some dishes. Write a program that tells you what recipe you can make based on the ingredient you have.

The input format:

A name of some ingredient.

The output format:

A message that says "food time!" where "food" stands for the dish that contains this ingredient. For example, "pizza time!". If the ingredient is featured in several recipes, write about all of them in the order they're featured in the cook book.

 Report a typo
Sample Input 1:

basil
Sample Output 1:

pasta time!
Sample Input 2:

flour
Sample Output 2:

apple pie time!
chocolate cake time!

'''

pasta = "tomato, basil, garlic, salt, pasta, olive oil"
apple_pie = "apple, sugar, salt, cinnamon, flour, egg, butter"
ratatouille = "aubergine, carrot, onion, tomato, garlic, olive oil, pepper, salt"
chocolate_cake = "chocolate, sugar, salt, flour, coffee, butter"
omelette = "egg, milk, bacon, tomato, salt, pepper"

ingred = [pasta, apple_pie, ratatouille, chocolate_cake, omelette]
names = ['pasta', 'apple pie', 'ratatouille', 'chocolate cake', 'omelette']
cook_book = dict(zip(ingred, names))

ing = input().strip().lower()
print("".join([f"{v} time!\n" for k, v in cook_book.items() if ing in k]))


'''2nd method'''
j = {"pasta": "tomato, basil, garlic, salt, pasta, olive oil",
     "apple pie": "apple, sugar, salt, cinnamon, flour, egg, butter",
     "ratatouille": "aubergine, carrot, onion, tomato, garlic, olive oil, pepper, salt",
     "chocolate cake": "chocolate, sugar, salt, flour, coffee, butter",
     "omelette": "egg, milk, bacon, tomato, salt, pepper"}

name_ingredient = input()
for i in j:
    if name_ingredient in j.get(i):
        print(f"{i} time!")


'''3rd Method'''
pasta = "tomato, basil, garlic, salt, pasta, olive oil"
apple_pie = "apple, sugar, salt, cinnamon, flour, egg, butter"
ratatouille = "aubergine, carrot, onion, tomato, garlic, olive oil, pepper, salt"
chocolate_cake = "chocolate, sugar, salt, flour, coffee, butter"
omelette = "egg, milk, bacon, tomato, salt, pepper"
recipes = [["pasta", pasta], ["apple pie", apple_pie], ["ratatouille", ratatouille], ["chocolate cake", chocolate_cake],
           ["omelette", omelette]]
ing = input()
for recipe in recipes:
    if ing in recipe[1]:
        print(recipe[0] + " time!")
