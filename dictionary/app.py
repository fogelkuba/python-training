import json
from difflib import SequenceMatcher, get_close_matches

data = json.load(open("./data.json"))

def translate(w):
    w = w.lower()
    get_close_matches(w, data.keys(), n = 3)
    if w in data:
        return data[w]
    elif len( get_close_matches(w, data.keys()) ) > 0:
        return "Did you mean %s instead?" % get_close_matches(w, data.keys())[0]
    else:
        return "The word doesn' exist. Please double check."

word = input("Enter word: ")

print(translate(word))