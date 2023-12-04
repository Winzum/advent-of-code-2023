from utils import read_input, sum_array
import re


def extract_card_numbers(line):
    card_pattern = re.compile(r"Card\s+(\d+):")
    return int(card_pattern.findall(line)[0])


def extract_cards(line):
    cards = line.split(":")[1].split("|")
    return [
        list(map(int, cards[0].strip().split())),
        list(map(int, cards[1].strip().split())),
    ]


def get_card_matches(winners, playing):
    matches = 0
    for p in playing:
        if p in winners:
            matches += 1
    return matches


def collect_winning_card_scores(cards):
    winning_card_scores = []
    for card in cards:
        matches = get_card_matches(cards[card][0], cards[card][1])
        if matches > 0:
            winning_card_scores.append(2 ** (matches - 1))
    return winning_card_scores


def collect_winning_card_counts(deck, cards):
    card_count = len(cards)
    # print(f"card_count: {card_count}")
    for card in cards:
        if cards == deck:
            print(f"checking: {card}: {cards[card]} = {card_count}")
        matches = get_card_matches(cards[card][0], cards[card][1])
        if matches > 0:
            bonus_cards = dict(
                (key, deck[key])
                for key in range(card + 1, min(card + matches + 1, len(deck)))
            )
            # print(f"bonus cards: {bonus_cards}")
            bonus_card_count = collect_winning_card_counts(deck, bonus_cards)
            # print(f"bonus card count: {bonus_card_count}")
            card_count += bonus_card_count
    return card_count


use_example = False
card_numbers = read_input(4, extract_card_numbers, use_example)
card_content = read_input(4, extract_cards, use_example)
cards = dict(zip(card_numbers, card_content))


# part 1
winning_card_scores = collect_winning_card_scores(cards)
print(sum_array(winning_card_scores))


# part 2
cards_amount = {card: 1 for card in card_numbers}
winning_card_counts = collect_winning_card_counts(cards, cards)
print(winning_card_counts)
