import json
from difflib import get_close_matches

data = json.load(open("datapython.json"))


def tranlate(word):
    if word in data:
        return data[word]
    elif word.title() in data:
        return data[word.title()]
    elif word.upper() in data:
        return data[word.upper()]
    elif word.lower() in data:
        return data[word.lower()]
    elif word.capitalize() in data:
        return data[word.capitalize()]
    elif len(get_close_matches(word, data.keys())) > 0:
        print(f'Did you means {get_close_matches(word, data.keys())[0]}: ')
        decide = input('Press y for yes or n for no: ')
        while decide not in "yn":
            decide = input('Press y for yes or n for no: ')
        if decide == "y":
            return data[get_close_matches(word, data.keys())[0]]
        elif decide == "n":
            return "Don't have this word"
    else:
        return "Don't have this word"

word = str(input("Enter with a word: ")).strip()
print(tranlate(word))


