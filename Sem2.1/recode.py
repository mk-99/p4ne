import json, random, time

random.seed(time.time())

table = [x for x in range(0, 10)]

num_swaps = random.randint(100, 500)

for x in range(num_swaps):
    pos1 = random.randint(0, 9)
    pos2 = random.randint(0, 9)
    while pos2 == pos1:
        pos2 = random.randint(0, 9)
    print("Swapping", pos1, pos2)
    table[pos1], table[pos2] = table[pos2], table[pos1]

print(table)

def recode(t, list):
    z = ""
    for x in list:
        z = z + str(t[int(x)])
    return z

with open('card2.json') as f:
    cards = json.load(f)

for c in cards:
    num = c['CreditCard']['CardNumber']
    num1 = recode(table, str(c['CreditCard']['CardNumber']))
    print(num1, num)
    del c['CreditCard']['CardNumber']
    c['CreditCard']['CardNumberCoded'] = str(num1)

print(cards)

with open('cardcoded.json', 'w') as f:
    json.dump(cards, f, indent=4)
