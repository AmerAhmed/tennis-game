"""This is a tennis game version 0.0.1
It has two classes TennisGam1 and TennisGame2.
wit different methods

    Returns:
        _type_: It returns value of type dict.
"""


class TennisGame1:
    """A class Tennisgame1 used to represent a tennisGame1 two methods
    and it returns value """

    def __init__(self, player1Name, player2Name):
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
        self.player1Name = player1Name
        self.player2Name = player2Name
        self.p1points = 0
        self.p2points = 0

    def won_point(self, playerName):
        """
        won_point function har one parameter playName 

        Args:
            playerName (String):
        """
        if playerName == self.player1Name:
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
        tempScore = 0
        if (self.p1points == self.p2points):
            result = {
                0: "Love-All",
                1: "Fifteen-All",
                2: "Thirty-All",
            }.get(self.p1points, "Deuce")
        elif (self.p1points >= 4 or self.p2points >= 4):
            minusResult = self.p1points-self.p2points
            if (minusResult == 1):
                result = "Advantage " + self.player1Name
            elif (minusResult == -1):
                result = "Advantage " + self.player2Name
            elif (minusResult >= 2):
                result = "Win for " + self.player1Name
            else:
                result = "Win for " + self.player2Name
        else:
            for i in range(1, 3):
                if (i == 1):
                    tempScore = self.p1points
                else:
                    result += "-"
                    tempScore = self.p2points
                result += {
                    0: "Love",
                    1: "Fifteen",
                    2: "Thirty",
                    3: "Forty",
                }[tempScore]
        return result


class TennisGame2:
    """We have here class TennisGame2 with the same functionalities
     as above.
    """

    def __init__(self, player1Name, player2Name):
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
        self.player1Name = player1Name
        self.player2Name = player2Name
        self.p1points = 0
        self.p2points = 0

    def won_point(self, playerName):
        """
        won_point function har one parameter playName

        Args:
            playerName (String)
        """
        if playerName == self.player1Name:
            self.P1Score()
        else:
            self.P2Score()

    def score(self):
        """
        score function takes care of player's score

        Returns:
            _type_:(String) It returns value of string
        """
        result = ""
        if (self.p1points == self.p2points and self.p1points < 3):
            if (self.p1points == 0):
                result = "Love"
            if (self.p1points == 1):
                result = "Fifteen"
            if (self.p1points == 2):
                result = "Thirty"
            result += "-All"
        if (self.p1points == self.p2points and self.p1points > 2):
            result = "Deuce"

        P1res = ""
        P2res = ""
        if (self.p1points > 0 and self.p2points == 0):
            if (self.p1points == 1):
                P1res = "Fifteen"
            if (self.p1points == 2):
                P1res = "Thirty"
            if (self.p1points == 3):
                P1res = "Forty"

            P2res = "Love"
            result = P1res + "-" + P2res
        if (self.p2points > 0 and self.p1points == 0):
            if (self.p2points == 1):
                P2res = "Fifteen"
            if (self.p2points == 2):
                P2res = "Thirty"
            if (self.p2points == 3):
                P2res = "Forty"

            P1res = "Love"
            result = P1res + "-" + P2res

        if (self.p1points > self.p2points and self.p1points < 4):
            if (self.p1points == 2):
                P1res = "Thirty"
            if (self.p1points == 3):
                P1res = "Forty"
            if (self.p2points == 1):
                P2res = "Fifteen"
            if (self.p2points == 2):
                P2res = "Thirty"
            result = P1res + "-" + P2res
        if (self.p2points > self.p1points and self.p2points < 4):
            if (self.p2points == 2):
                P2res = "Thirty"
            if (self.p2points == 3):
                P2res = "Forty"
            if (self.p1points == 1):
                P1res = "Fifteen"
            if (self.p1points == 2):
                P1res = "Thirty"
            result = P1res + "-" + P2res

        if (self.p1points > self.p2points and self.p2points >= 3):
            result = "Advantage " + self.player1Name

        if (self.p2points > self.p1points and self.p1points >= 3):
            result = "Advantage " + self.player2Name

        if (self.p1points >= 4 and self.p2points >= 0 and (self.p1points-self.p2points) >= 2):
            result = "Win for " + self.player1Name
        if (self.p2points >= 4 and self.p1points >= 0 and (self.p2points-self.p1points) >= 2):
            result = "Win for " + self.player2Name
        return result

    def SetP1Score(self, number):
        """
        SetP1Score function set player1 score.

        Args:
            number (Integer): It returns value of numbers for player's score.
        """
        for i in range(number):
            self.P1Score()

    def SetP2Score(self, number):
        """
        SetP2Score function set player2 score

        _extended_summary_

        Args:
            number (Integer): It returns value of numbers for player's score.
        """
        for i in range(number):
            self.P2Score()

    def P1Score(self):
        """
        P1Score function increases player1's score with 1
        """
        self.p1points += 1

    def P2Score(self):
        """
        P2Score function increases player2's score with 1
        """
        self.p2points += 1
