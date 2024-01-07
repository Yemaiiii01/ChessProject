import random
import json

class Tournament:
    def __init__(self, name, venue, start_date, end_date):
        self.name = name
        self.venue = venue
        self.start_date = start_date
        self.end_date = end_date
        self.players = []  # List of Player objects
        self.rounds = []  # List of Round objects
        self.current_round = 0
        self.scores = {player: 0 for player in self.players}

    def add_player(self, player):
        self.players.append(player)
        self.scores[player] = 0

    def start_next_round(self):
        if self.current_round == 0:
            pairings = self._pair_players()
        else:
            pairings = self._pair_players_based_on_scores()
        round_matches = [Match(p1, p2) for p1, p2 in pairings]
        self.rounds.append(round_matches)
        self.current_round += 1

    def _pair_players(self):
        shuffled_players = random.sample(self.players, len(self.players))
        return [(shuffled_players[i], shuffled_players[i + 1]) for i in range(0, len(shuffled_players), 2)]

    def _pair_players_based_on_scores(self):
        # Implement the logic for pairing based on tournament scores
        pass

    def record_match_result(self, round_number, match_number, winner):
        match = self.rounds[round_number][match_number]
        match.set_result(winner)
        self.scores[winner] += 1

    def to_dict(self):
        return {
            'name': self.name,
            'venue': self.venue,
            'start_date': self.start_date,
            'end_date': self.end_date,
            'players': [player.to_dict() for player in self.players],
            'rounds': [[match.to_dict() for match in round] for round in self.rounds]
        }

    @staticmethod
    def load_from_file(file_name):
        with open(file_name, 'r') as file:
            data = json.load(file)
        tournament = Tournament(data['name'], data['venue'], data['start_date'], data['end_date'])
        for player_data in data['players']:
            tournament.add_player(Player(**player_data))
        return tournament


class Match:
    def __init__(self, player1, player2):
        self.player1 = player1
        self.player2 = player2
        self.result = None  # Result of the match

    def set_result(self, winner):
        self.result = winner

    def to_dict(self):
        return {
            'player1': self.player1.to_dict(),
            'player2': self.player2.to_dict(),
            'result': self.result.to_dict() if self.result else None
        }
