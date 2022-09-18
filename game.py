"""This is a Tennis-Game"""


class TennisGame:
    """A class Tennis_game used to represent a tennisGame1 two methods"""

    def __init__(self, player_name: str, points: int = 0) -> None:
        """
            __init__ takes two parameters player1_name and player2_name

            Args:
                player_name: string
                           The name of player1
                    points:
                           The player points
        """
        self.player_name = player_name
        self.points = points

    def won_point(self, player_name: str) -> str:
        """
        won_point function har one parameter player_name

        Args:
            player_name (String):
        """
        if player_name == self.player1_name:
            self.player1_points += 1
        else:
            self.player2_points += 1
        return player_name

    @property
    def score(self):
        """
        score function takes care of player's score

        Returns:
            _type_: (String) it returns value of string
        """
        result = ""
        temp_score = 0
        if self.player1_points == self.player2_points:
            result = {
                0: "Love-All",
                1: "Fifteen-All",
                2: "Thirty-All",
            }.get(self.player1_points, "Deuce")
        elif self.player1_points >= 4 or self.player2_points >= 4:
            minus_result = self.player1_points - self.player2_points
            if minus_result == 1:
                result = "Advantage " + self.player1_name
            elif minus_result == -1:
                result = "Advantage " + self.player2_name
            elif minus_result >= 2:
                result = "Win for " + self.player1_name
            else:
                result = "Win for " + self.player2_name
        else:
            for i in range(1, 3):
                if i == 1:
                    temp_score = self.player1_points
                else:
                    result += "-"
                    temp_score = self.player2_points
                result += {
                    0: "Love",
                    1: "Fifteen",
                    2: "Thirty",
                    3: "Forty",
                }[temp_score]
        return result


player1 = TennisGame('Ahmed', 'Amer')
player2 = TennisGame('Adam', 'Ali')

print(player1.won_point('Amer'))
print(player2.won_point('Ahmed'))

print(player1.score)

print(player2.score)
