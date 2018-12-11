import json
import difflib
from difflib import SequenceMatcher, get_close_matches

data = json.load(open("./data.json"))

def translate(w):
    w = w.lower()

    get_close_matches(w, data.keys(), n = 3)

    if w in data:
        return data[w]
    else:
        return "The word doesn' exist. Please double check."

word = input("Enter word: ")

print(translate(word))