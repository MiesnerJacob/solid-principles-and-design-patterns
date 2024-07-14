class Player:
    def __init__(self, name, position, number):
        self.name = name
        self.position = position
        self.number = number


class Team:
    def __init__(self, name):
        self.name = name
        self.players: List[Player] = []

    def add_player(self, player):
        self.players.append(player)

    def get_player_info(self, number):
        for player in self.players:
            if player.number == number:
                return f"{player.name} ({player.position}) - {player.number}"
        return "Player not found."\


if __name__ == "__main__":
    # Test your implementation
    player1 = Player("John Doe", "Forward", 10)
    player2 = Player("Jane Smith", "Midfielder", 8)
    player3 = Player("Mark Johnson", "Defender", 4)

    team1 = Team("Dream Team")
    team1.add_player(player1)
    team1.add_player(player2)

    print(team1.get_player_info(10))  # Should output "John Doe (Forward) - 10"
    print(team1.get_player_info(8))   # Should output "Jane Smith (Midfielder) - 8"
    print(team1.get_player_info(4))   # Should output "Player not found"