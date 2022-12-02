from typing import Literal

from helpers import read_file_as_list

rounds = read_file_as_list("./data/2.csv", lambda x: x.split(), "")

class Node:
    def __init__(self, score: int):
        self.score = score
        self.beats = None

# 2.a

Rock = Node(1)
Paper = Node(2)
Scissor = Node(3)

name_to_hand = {
    "A": Rock,
    "B": Paper,
    "C": Scissor,
    "X": Rock,
    "Y": Paper,
    "Z": Scissor
}

Rock.beats = Scissor
Scissor.beats = Paper
Paper.beats = Rock


def score_round(hand1: Node, hand2: Node):
    if hand1 is hand2:
        return hand1.score + 3

    if hand1.beats is hand2:
        return hand1.score + 6

    return hand1.score + 0


total_score = 0
for round in rounds:
    player_hand = name_to_hand[round[1]]
    opponent_hand = name_to_hand[round[0]]
    total_score += score_round(player_hand, opponent_hand)
print(total_score)

# 2.b
def score_round(opp_hand: Node, outcome: Literal["X", "Y", "Z"]):
    if outcome == "X":
       return opp_hand.beats.score
    if outcome == "Y":
        return opp_hand.score + 3
    return opp_hand.beats.beats.score + 6

total_score = 0
for round in rounds:
    opponent_hand = name_to_hand[round[0]]
    outcome = round[1]
    total_score += score_round(opponent_hand, outcome)
print(total_score)
