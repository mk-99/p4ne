import requests
import argparse
import pprint


parser = argparse.ArgumentParser(description="Get bank cards info")

parser.add_argument("cards", nargs="*", help="First 8 digits of card number")

args = parser.parse_args()

for card in args.cards:
    r = requests.get('https://lookup.binlist.net/' + card, headers={'Accept-Version': "3"})
    if r.status_code == 200:
        pprint.pprint(r.json())
    else:
        print("Card", card, "error code ", r.status_code)
