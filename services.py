import json


def write_json(calories_dict):
    with open('calories.json', 'w') as file:
        json.dump(calories_dict, file, indent=2, ensure_ascii=False)


def read_json(filename):
    with open(filename, 'r') as file:
        return json.load(file)
