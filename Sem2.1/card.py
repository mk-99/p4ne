import requests
import argparse
import pprint
import json


parser = argparse.ArgumentParser(description="Get bank cards info")
parser.add_argument("cards", nargs="*", help="First 8 digits of card number")
parser.add_argument("-f", "--file", help="File name for JSON data")

args = parser.parse_args()

card_numbers = []

if args.file:
    with open(args.file) as f:
        l = json.load(f)
        card_numbers += [str(x['CreditCard']['CardNumber'])[0:8] for x in l]

for arg_card in args.cards:
    card_numbers.append(arg_card)

banks = set()

for card_no in card_numbers:
    r = requests.get('https://lookup.binlist.net/' + card_no, headers={'Accept-Version': "3"})
    if 200 <= r.status_code <= 299:
        current_card = r.json()
        pprint.pprint(current_card)
        if current_card['bank']:
            bank_name = current_card['bank']['name']
            print(bank_name)
            banks.add(bank_name)
    else:
        print("Card", card_no, "error code ", r.status_code)

pprint.pprint(sorted(list(banks)))
