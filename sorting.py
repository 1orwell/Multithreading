animals = ['cat', 'dog', 'cheetah', 'rhino']
#print(sorted(animals))
#print(sorted(animals, reverse=True))

animals_dict = [
    {'type':'cat', 'name':'Spot', 'age':12},
    {'type':'dog', 'name':'Rose', 'age':4},
    {'type':'cheetah', 'name':'Sue', 'age':3},
]

for animal in animals_dict:
    print(animal['type'])

print([animal['type'] for animal in animals_dict])

sorted_dict = sorted(animals_dict, key = lambda animal : animal['age'])
print(sorted_dict)