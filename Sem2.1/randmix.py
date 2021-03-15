import json
import random

with open('carddata.json') as f:
    l = json.load(f)

random.shuffle(l)

i = random.randint(0, 70)

with open('card1.json', 'w') as f:
    json.dump(l[i:i+30], f, indent=4)
