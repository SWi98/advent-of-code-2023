from utils.file_operations import read_lines
from functools import total_ordering
from enum import Enum


class HandType(Enum):
    FIVE = 6
    FOUR = 5
    FULL_HOUSE = 4
    THREE = 3
    TWO_PAIRS = 2
    ONE_PAIR = 1
    HIGH_CARD = 0


CARD_STRENGHT_MAPPING = {
    "A": 14,
    "K": 13,
    "Q": 12,
    "J": 11,
    "T": 10
}


def get_card_strenght(card: str) -> int:
    if card.isnumeric():
        return int(card)
    else:
        return CARD_STRENGHT_MAPPING[card]


@total_ordering
class Hand:
    def __init__(self, cards: str, bid: int):
        self.og_cards = cards
        self.bid = int(bid)
        split_cards = list(cards)
        self.cards = [get_card_strenght(card) for card in split_cards]
        self.unique_cards = set(self.cards)
        self.hand_type = self.define_hand_type()

    def define_hand_type(self) -> HandType:
        cards_amount = {card: 0 for card in list(self.unique_cards)}
        for card in self.cards:
            cards_amount[card] += 1
        threes = 0
        pairs = 0
        for value in cards_amount.values():
            if value == 5:
                return HandType.FIVE
            if value == 4:
                return HandType.FOUR
            if value == 3:
                threes += 1
            if value == 2:
                pairs += 1
        if threes == 1:
            if pairs == 1:
                return HandType.FULL_HOUSE
            elif pairs == 0:
                return HandType.THREE
            else:
                raise ValueError(f"{pairs} pairs found")
        elif threes == 0:
            if pairs == 2:
                return HandType.TWO_PAIRS
            elif pairs == 1:
                return HandType.ONE_PAIR
            elif pairs == 0:
                return HandType.HIGH_CARD
            else:
                raise ValueError(f"{pairs} pairs found")
        else:
            raise ValueError(f"{threes} threes found")
        
    def __eq__(self, __value: "Hand") -> bool:
        if self.hand_type == __value.hand_type:
            for my_card, their_hard in zip(self.cards, __value.cards):
                if my_card != their_hard:
                    return False
            return True
        else:
            return False
        
    def __lt__(self, __value: "Hand") -> bool:
        print(f"Comparing {self.og_cards} to {__value.og_cards}")
        print(self.cards, __value.cards)
        if self.hand_type == __value.hand_type:
            for my_card, their_card in zip(self.cards, __value.cards):
                if my_card < their_card:
                    print(f"MY CARD {my_card} < THEIR CARD {their_card}")
                    return True
                elif my_card > their_card:
                    return False
            return False
        else:
            return self.hand_type.value < __value.hand_type.value


def main():
    lines = read_lines("7_1/input.txt", rstrip=True)
    # lines = read_lines("7_1/test_input.txt", rstrip=True)
    hands: list[Hand] = []
    for line in lines:
        hands.append(Hand(*line.split()))
    hands.sort()
    res = 0
    for i, hand in enumerate(hands):
        res += (i + 1) * hand.bid
        print(hand.og_cards)
    print(res)

if __name__ == "__main__":
    main()
