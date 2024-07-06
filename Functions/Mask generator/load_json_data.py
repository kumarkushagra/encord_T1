import json


def load_json_data(json_path):
    with open(json_path,'r') as file:
        data = json.load(file)
    return data
