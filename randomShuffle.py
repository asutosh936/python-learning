import random

cats = []

while True:
    print('Enter the name of cat ' + str(len(cats) + 1) + ' (Or enter nothing to stop.):')
    name = input()
    if name == '':
        break
    cats = cats + [name]  # list concatenation

print('The cat names are:' + str(cats))
print('Random choice of cat is: ' + random.choice(cats))
random.shuffle(cats)
print('Shuffled cat names are:' + str(cats))