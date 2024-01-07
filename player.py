class Player:
    def __init__(self, name, email, chess_id, birthdate):
        self.name = name
        self.email = email
        self.chess_id = chess_id
        self.birthdate = birthdate

    def __str__(self):
        return f"{self.name} (ID: {self.chess_id})"

    def to_dict(self):
        return {
            'name': self.name,
            'email': self.email,
            'chess_id': self.chess_id,
            'birthdate': self.birthdate
        }
