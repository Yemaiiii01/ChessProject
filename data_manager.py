import json
import os

def read_json_file(file_path):
    if not os.path.exists(file_path):
        return {}
    with open(file_path, 'r') as file:
        return json.load(file)

def write_json_file(file_path, data):
    with open(file_path, 'w') as file:
        json.dump(data, file, indent=4)

def load_clubs():
    clubs = []
    for file_name in os.listdir('data/clubs'):
        clubs.append(Club.load_from_file(f'data/clubs/{file_name}'))
    return clubs

def load_tournaments():
    tournaments = []
    for file_name in os.listdir('data/tournaments'):
        tournaments.append(Tournament.load_from_file(f'data/tournaments/{file_name}'))
    return tournaments


