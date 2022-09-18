"""This is a tennis game version 0.0.1
It has two classes TennisGam1 and TennisGame2.
wit different methods

    Returns:
        _type_: It returns value of type dict.
"""


class TennisGame1:
    """A class Tennisgame1 used to represent a tennisGame1 two methods
    and it returns value """

    def __init__(self, player1_name, player2_name):
        """
        __init__ takes two parameters player1Nmae and player2Name

        Args:
            player1Name: string
                    The name of player1
            player2Name: string
                    The name of player2
            p1points: Integer
                    The numbers of points of player1
            p2points: Integer
                    The numbers of points of player2
        """
        self.player1_name = player1_name
        self.player2_name = player2_name
        self.p1points = 0
        self.p2points = 0

    def won_point(self, player_name):
        """
        won_point function har one parameter playName

        Args:
            playerName (String):
        """
        if player_name == self.player1_name:
            self.p1points += 1
        else:
            self.p2points += 1

    def score(self):
        """
        score function takes care of player's score

        Returns:
            _type_: (String) it returns value of string
        """
        result = ""
        temp_score = 0
        if self.p1points == self.p2points:
            result = {
                0: "Love-All",
                1: "Fifteen-All",
                2: "Thirty-All",
            }.get(self.p1points, "Deuce")
        elif (self.p1points >= 4 or self.p2points >= 4):
            minus_result = self.p1points-self.p2points
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
                    temp_score = self.p1points
                else:
                    result += "-"
                    temp_score = self.p2points
                result += {
                    0: "Love",
                    1: "Fifteen",
                    2: "Thirty",
                    3: "Forty",
                }[temp_score]
        return result


class TennisGame2:
    """We have here class TennisGame2 with the same functionalities
     as above.
    """

    def __init__(self, player1_name, player2_name):
        """
        __init__ takes two parameters player1Nmae and player2Name

        Args:
            player1Name: string
                    The name of player1
            player2Name: string
                    The name of player2
            p1points: Integer
                    The numbers of points of player1
            p2points: Integer
        """
        self.player1_name = player1_name
        self.player2_name = player2_name
        self.p1points = 0
        self.p2points = 0

    def won_point(self, player_name):
        """
        won_point function har one parameter playName

        Args:
            playerName (String)
        """
        if player_name == self.player1_name:
            self.player1_score()
        else:
            self.player2_score()

    def score(self):
        """
        score function takes care of player's score

        Returns:
            _type_:(String) It returns value of string
        """
        result = ""
        if (self.p1points == self.p2points and self.p1points < 3):
            if self.p1points == 0:
                result = "Love"
            if self.p1points == 1:
                result = "Fifteen"
            if self.p1points == 2:
                result = "Thirty"
            result += "-All"
        if (self.p1points == self.p2points and self.p1points > 2):
            result = "Deuce"

        player1_result = ""
        player2_result = ""
        if (self.p1points > 0 and self.p2points == 0):
            if self.p1points == 1:
                player1_result = "Fifteen"
            if self.p1points == 2:
                player1_result = "Thirty"
            if self.p1points == 3:
                player1_result = "Forty"

            player2_result = "Love"
            result = player1_result + "-" + player2_result
        if self.p2points > 0 and self.p1points == 0:
            if self.p2points == 1:
                player2_result = "Fifteen"
            if self.p2points == 2:
                player2_result = "Thirty"
            if self.p2points == 3:
                player2_result = "Forty"

            player1_result = "Love"
            result = player1_result + "-" + player2_result

        if self.p1points > self.p2points and self.p1points < 4:
            if self.p1points == 2:
                player1_result = "Thirty"
            if self.p1points == 3:
                player1_result = "Forty"
            if self.p2points == 1:
                player2_result = "Fifteen"
            if self.p2points == 2:
                player2_result = "Thirty"
            result = player1_result + "-" + player2_result
        if self.p2points > self.p1points and self.p2points < 4:
            if self.p2points == 2:
                player2_result = "Thirty"
            if self.p2points == 3:
                player2_result = "Forty"
            if self.p1points == 1:
                player1_result = "Fifteen"
            if self.p1points == 2:
                player1_result = "Thirty"
            result = player1_result + "-" + player2_result

        if (self.p1points > self.p2points and self.p2points >= 3):
            result = "Advantage " + self.player1_name

        if (self.p2points > self.p1points and self.p1points >= 3):
            result = "Advantage " + self.player2_name

        if (self.p1points >= 4 and self.p2points >= 0 and (self.p1points-self.p2points) >= 2):
            result = "Win for " + self.player1_name
        if (self.p2points >= 4 and self.p1points >= 0 and (self.p2points-self.p1points) >= 2):
            result = "Win for " + self.player2_name
        return result

    def setplayer1_score(self, number):
        """
        SetP1Score function set player1 score.

        Args:
            number (Integer): It returns value of numbers for player's score.
        """
        for _ in range(number):
            self.player1_score()

    def setplayer2_score(self, number):
        """
        SetP2Score function set player2 score

        _extended_summary_

        Args:
            number (Integer): It returns value of numbers for player's score.
        """
        for _ in range(number):
            self.player2_score()

    def player1_score(self):
        """
        P1Score function increases player1's score with 1
        """
        self.p1points += 1

    def player2_score(self):
        """
        P2Score function increases player2's score with 1
        """
        self.p2points += 1

players = ['Amer', 'Ahmed']
player1 = TennisGame1(players[0])

print(players.won_point(10))
