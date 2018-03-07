import json
from pprint import pprint

with open('train.json') as data_file:
    data = json.load(data_file)
pprint(type(data['recipes']))

listOfIngredients = []
for cuisine in data['recipes']:
    ingredients = cuisine['ingredients']
    for oneIngredient in ingredients:
        listOfIngredients.append(oneIngredient)
setOfIngredients = set(listOfIngredients)
uniqueIngredients = list(setOfIngredients)
uniqueIngredients.sort()
print(uniqueIngredients)
with open('output.json', 'w') as outfile:
    json.dump(uniqueIngredients, outfile)

