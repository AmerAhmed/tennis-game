"""
The main point module for Tennsi-Game
@Author: Amer Ahmed
Supervisor: Ammar Alnahhas
TennisGmae: Version 1.0.0
"""

from tennis_v1 import TennisGame, Match


def main():
    """main function to run"""
amer_ahmed = TennisGame("Amer Ahmed", 100000)
sara_adam = TennisGame("Sara Adam", 100000)

test_match = Match(amer_ahmed, sara_adam)
test_match.play_match()

if __name__ == 'main':
    main()
    