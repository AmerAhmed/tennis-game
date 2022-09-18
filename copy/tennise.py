"""
     _summary_

    _extended_summary_

    Returns:
        _type_: _description_
"""
import random


class TennisGame:
    """_extended_summary_
    """

    def __init__(self, name="", points=0):
        self.name = name
        self.points = points

    def update_points(self, points_update):
        """
        update_points _summary_

        _extended_summary_

        Args:
            points_update (_type_): _description_
        """
        self.points += points_update

    def __str__(self):
        return self.name

    def __repr__(self):
        return (
            f"Player(name='{self.name}', "
            f"points={self.points})"
        )


class Unit:
    """
     _summary_

    _extended_summary_
    """

    def __init__(self, players=(TennisGame(), TennisGame())):
        self.players = players
        self.score = {
            self.players[0]: 0,  # The key is of type Player
            self.players[1]: 0,
        }
        self.winner = None
        self.winner = None
        self.ranking_ratio = self.players[0].points / (
            self.players[0].points
            + self.players[1].points
        )

    def get_winner(self):
        """
        get_winner _summary_

        _extended_summary_

        Returns:
            _type_: _description_
        """
        return self.winner

    def get_score(self):
        """
        get_score _summary_

        _extended_summary_

        Returns:
            _type_: _description_
        """
        return self.score

    def is_running(self):
        """
        is_running _summary_

        _extended_summary_

        Returns:
            _type_: _description_
        """
        return self.winner is None


class Match(Unit):
    """
    Match _summary_

    _extended_summary_

    Args:
        Unit (_type_): _description_
    """

    def __init__(
            self,
            player_1=TennisGame(),
            player_2=TennisGame(),
            best_of_5=True,
    ):
        super().__init__(players=(player_1, player_2))
        self.best_of_5 = best_of_5
        self.sets_to_play = 5 if best_of_5 else 3
        self.sets = []
        self.simulated = False
        self.display_results = True

    def simulate_match(self):
        """
        simulate_match _summary_

        _extended_summary_
        """
        self.simulated = True

    def suppress_output(self):
        """
        suppress_output _summary_

        _extended_summary_
        """
        self.display_results = False

    def play_set(self):
        """
        play_set _summary_

        _extended_summary_
        """
        _set = Set(self, len(self.sets) + 1)
        self.sets.append(_set)

        while _set.is_running():
            _set.play_game()
        set_winner = _set.get_winner()
        # Update set score for player who won set
        self.score[set_winner] += 1

        # If player has won 2 sets if best-of-three
        # or 3 sets if best-of-five, match is over
        if self.score[set_winner] == self.sets_to_play // 2 + 1:
            self.winner = set_winner

    def play_match(self):
        """
        play_match _summary_

        _extended_summary_
        """
        while self.is_running():
            self.play_set()
        if self.display_results:
            print(f"\nWinner: {self.winner}")
            print(f"Score: {self}")

    def __str__(self):
        return " ".join([str(set) for _set in self.sets])

    def __repr__(self):
        return (
            f"Match("
            f"player_1={self.players[0]}, "
            f"player_2={self.players[1]}, "
            f"best_of_5={self.best_of_5})"
        )


class Set(Unit):
    """
    Set _summary_

    _extended_summary_

    Args:
        Unit (_type_): _description_
    """

    def __init__(self, match: Match, set_number=0):
        super().__init__(match.players)
        self.match = match
        self.set_number = set_number
        self.games = []
        self.simulated = False

    def simulate_match(self):
        """
        simulate_match _summary_

        _extended_summary_
        """
        self.simulated = True

    def play_game(self, tiebreak=False):
        """
        play_game _summary_

        _extended_summary_

        Args:
            tiebreak (bool, optional): _description_. Defaults to False.
        """
        # Creat a Game object and append to .games list
        if tiebreak:
            game = Tiebreak(self, len(self.games) + 1)
        else:
            game = Game(self, len(self.games) + 1)
        self.games.append(game)

        # Ask for user input to record who won point
        print(
            f"\nRecord point winner: "
            f"Press 1 for {self.players[0]} | "
            f"Press 2 for {self.players[1]}"
        )

        # If match is simulated, assign points randomly,
        # otherwise, ask user to record who won each point
        while game.is_running():
            if self.match.simulated:
                point_winner_idx = int(
                    random.random() > self.ranking_ratio
                )
            else:
                point_winner_idx = (
                    int(input("\nPoint Winner (1 or 2) -> ")) - 1
                )
            game.score_point(self.players[point_winner_idx])
            if self.match.display_results:
                print(game)

        # Game over - update set score
        self.score[game.winner] += 1
        if self.match.display_results:
            print(f"\nGame {game.winner.name}")
            print(f"\nCurrent score: {self.match}")

        # Check stage within set
        # If it's an early stage of the set and no one
        # reached 6 or 7 games, there's nothing else to do
        # and method can return
        if (
                6 not in self.score.values()
                and 7 not in self.score.values()
        ):
            return

        # Rest deals with latter stages of set when at least
        # one player is on 6 games
        # Check for 6-6 score
        if list(self.score.values()) == [6, 6]:
            self.play_game(tiebreak=True)
            return
        # …7-5 or 7-6 score (if tiebreak was played, score
        # will be 7-6)
        for player in self.players:
            # player reaches 7 games
            if self.score[player] == 7:
                self.winner = player
                return
            # player reaches 6 games
            # and 6-6 and 7-6 already ruled out
            if self.score[player] == 6:
                # Exclude 6-5 scenario
                if 5 not in self.score.values():
                    self.winner = player

    def __str__(self):
        return "-".join(
            [str(value) for value in self.score.values()]
        )

    def __repr__(self):
        return (
            f"Set(match={self.match!r}, "
            f"set_number={self.set_number})"
        )


class Game(Unit):
    """
    Game _summary_

    _extended_summary_

    Args:
        Unit (_type_): _description_

    Returns:
        _type_: _description_
    """
    points = 0, 15, 30, 40, "Ad"  # Class attribute

    def __init__(self, _set: Set, game_number=0):
        super().__init__(_set.match.players)
        self.set = set
        self.game_number = game_number

    def score_point(self, player: TennisGame):
        """
        score_point _summary_

        _extended_summary_

        Args:
            player (TennisGame): _description_
        """
        if self.winner:
            print(
                "Error: You tried to add a point to a completed game"
            )
            return
        game_won = False
        current_point = self.score[player]
        # Player who wins point was on 40
        if self.score[player] == 40:
            # Other player is on Ad
            if "Ad" in self.score.values():
                # Update both players' scores to 40
                for each_player in self.players:
                    self.score[each_player] = 40
            # Other player is also on 40 (deuce)
            elif list(self.score.values()) == [40, 40]:
                # Point winner goes to Ad
                self.score[player] = "Ad" # type: ignore
            # Other player is on 0, 15, or 30
            else:
                # player wins the game
                game_won = True
        # Player who wins point was on Ad
        elif self.score[player] == "Ad":
            # player wins the game
            game_won = True
        # Player who wins point is on 0, 15, or 30
        else:
            self.score[player] = Game.points[  # type: ignore
                Game.points.index(current_point) + 1
            ]

        if game_won:
            self.score[player] = "Game"
            self.winner = player

    def __str__(self):
        score_values = list(self.score.values())
        return f"{score_values[0]} - {score_values[1]}"

    def __repr__(self):
        return (
            f"{self.__class__.__name__}(set={self.set!r}, "
            f"game_number={self.game_number})"
        )


class Tiebreak(Game):
    """
    Tiebreak _summary_

    _extended_summary_

    Args:
        Game (_type_): _description_
    """

    def __init__(self, _set: Set, game_number=0):  # type: ignore
        super().__init__(_set, game_number)

    def score_point(self, player: TennisGame):
        if self.winner:
            print(
                "Error: You tried to add a point to a completed game"
            )
            return
        # Add point to player
        self.score[player] += 1
        # Tiebreak over only if player has 7 or more points
        # and there's at least a 2 point-gap
        if (
                self.score[player] >= 7
                and self.score[player] - min(self.score.values()) >= 2
        ):
            self.winner = player
