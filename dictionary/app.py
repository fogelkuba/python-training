import json
import difflib
from difflib import SequenceMatcher

data = json.load(open("./data.json"))

def translate(w):
    w = w.lower()
    if w in data:
        return data[w]
    else:
        return "The word doesn' exist. Please double check."

word = input("Enter word: ")

print(translate(word))