import json
from difflib import SequenceMatcher, get_close_matches

data = json.load(open("./data.json"))

def translate(w):
    w = w.lower()
    get_close_matches(w, data.keys(), n = 3)
    if w in data:
        return data[w]
    elif len( get_close_matches(w, data.keys()) ) > 0:
        confirm = input("Did you mean %s instead? Enter Y if yes, N if no:" % get_close_matches(w, data.keys())[0])
        if confirm.lower() == "y":
            return data[get_close_matches(w, data.keys())[0]]
        elif confirm.lower() == "n":
            return "The word doesn't exist. Please double check."
        else:
            return "We didn't understand your query."
    else:
        return "The word doesn't exist. Please double check."

word = input("Enter word: ")

print(translate(word))