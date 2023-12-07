from utils import read_input, sum_array
from collections import defaultdict

# either one of the "J" should be commented out depending on part 1 or part 2
card_order = {
    "J": 1,
    "2": 2,
    "3": 3,
    "4": 4,
    "5": 5,
    "6": 6,
    "7": 7,
    "8": 8,
    "9": 9,
    "T": 10,
    # "J": 11,
    "Q": 12,
    "K": 13,
    "A": 14,
}


def extract_hand(line):
    hand = line.split()
    return [[card for card in hand[0]], int(hand[1])]


def check_hand(hand):
    cards = hand[0]
    # print(cards)
    Joker = 0
    for card in cards:
        if card == "J":
            Joker += 1

    value_counts = defaultdict(lambda: 0)
    for card in cards:
        value_counts[card] += 1
    # print(value_counts)

    sorted_value_count = sorted(value_counts.values())
    match Joker:
        case 4:
            # five of a kind
            return 0
        case 3:
            match sorted_value_count:
                # five of a kind
                case [2, 3]:
                    return 0
                # four of a kind
                case [1, 1, 3]:
                    return 1
        case 2:
            match sorted_value_count:
                # five of a kind
                case [2, 3]:
                    return 0
                # four of a kind
                case [1, 2, 2]:
                    return 1
                # three of a kind
                case [1, 1, 1, 2]:
                    return 3

        case 1:
            match sorted_value_count:
                # five of a kind
                case [1, 4]:
                    return 0
                # four of a kind
                case [1, 1, 3]:
                    return 1
                # full house
                case [1, 2, 2]:
                    return 2
                # three of a kind
                case [1, 1, 1, 2]:
                    return 3
                # one pair
                case [1, 1, 1, 1, 1]:
                    return 5

        case _:
            match sorted_value_count:
                # five of a kind
                case [5]:
                    return 0
                # four of a kind
                case [1, 4]:
                    return 1
                # full house
                case [2, 3]:
                    return 2
                # three of a kind
                case [1, 1, 3]:
                    return 3
                # two pair
                case [1, 2, 2]:
                    return 4
                # one pair
                case [1, 1, 1, 2]:
                    return 5
                # high card
                case _:
                    return 6


five_of_a_kind = []
four_of_a_kind = []
full_house = []
three_of_a_kind = []
two_pair = []
one_pair = []
high_card = []
hands_collection = [
    five_of_a_kind,
    four_of_a_kind,
    full_house,
    three_of_a_kind,
    two_pair,
    one_pair,
    high_card,
]
hands_ranking = []


def sort_hand_list(hand_list):
    sorted_hand_list = list(
        reversed(sorted(hand_list, key=lambda x: [card_order[card] for card in x[0]]))
    )
    return sorted_hand_list


# part 1 & 2
hands = read_input(7, extract_hand, False)
# print(hands)
for hand in hands:
    hands_collection[check_hand(hand)].append(hand)

for hand_list in hands_collection:
    sorted_hand_list = sort_hand_list(hand_list)
    for sorted_hand in sorted_hand_list:
        hands_ranking.append(sorted_hand)

winnings = []
for idx, hand in enumerate(list(reversed(hands_ranking))):
    winnings.append(hand[1] * (idx + 1))

print(sum_array(winnings))
