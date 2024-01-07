import json
import os

class Club:
    def __init__(self, name):
        self.name = name
        self.players = []  # List of Player objects

    def add_player(self, player):
        self.players.append(player)

    def get_players(self):
        return self.players

    def save_to_file(self):
        if not os.path.exists('data/clubs'):
            os.makedirs('data/clubs')
        with open(f'data/clubs/{self.name}.json', 'w') as file:
            json.dump(self.to_dict(), file, indent=4)

    def to_dict(self):
        return {
            'name': self.name,
            'players': [player.to_dict() for player in self.players]
        }

    @staticmethod
    def load_from_file(file_name):
        with open(file_name, 'r') as file:
            data = json.load(file)
        club = Club(data['name'])
        for player_data in data['players']:
            club.add_player(Player(**player_data))
        return club

