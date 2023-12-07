from utils.file_operations import read_lines
from functools import total_ordering
from enum import Enum
import queue


class HandType(Enum):
    FIVE = 6
    FOUR = 5
    FULL_HOUSE = 4
    THREE = 3
    TWO_PAIRS = 2
    ONE_PAIR = 1
    HIGH_CARD = 0


CARD_STRENGHT_MAPPING = {
    "A": 13,
    "K": 12,
    "Q": 11,
    "J": 1,
    "T": 10
}


def get_card_strenght(card: str) -> int:
    if card.isnumeric():
        return int(card)
    else:
        return CARD_STRENGHT_MAPPING[card]


def construct_possible_cards(cards: list[int]) -> list[list[int]]:
    n = len(cards)
    res = []
    hands_to_handle: queue.Queue[list[int]] = queue.Queue()
    hands_to_handle.put(cards)
    while not hands_to_handle.empty():
        hand = hands_to_handle.get()
        if 1 not in hand:
            res.append(hand)
        else:
            joker_idx = hand.index(1)
            for strength in range(2, 14):
                new_hand = hand.copy()
                new_hand[joker_idx] = strength
                hands_to_handle.put(new_hand)
    return res
    

@total_ordering
class Hand:
    def __init__(self, cards: str, bid: int):
        self.og_cards = cards
        self.bid = int(bid)
        split_cards = list(cards)
        self.cards = [get_card_strenght(card) for card in split_cards]
        self.best_cards = self.cards
        possible_hands = construct_possible_cards(self.cards)
        self.hand_type = self.define_hand_type(self.cards)
        for hand in possible_hands:
            hand_type = self.define_hand_type(hand)
            # print(f"Analyzing {hand} for {self.og_cards}. It gave {hand_type}; val: {hand_type.value}")
            if hand_type.value > self.hand_type.value:
                self.hand_type = hand_type
                self.best_cards = hand
        # print("Selected type:", self.hand_type)

    def define_hand_type(self, cards: list[int]) -> HandType:
        unique_cards = set(cards)
        cards_amount = {card: 0 for card in list(unique_cards)}
        for card in cards:
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
        # print(f"Comparing {self.og_cards} to {__value.og_cards}")
        # print(self.cards, __value.cards)
        # print(self.best_cards, __value.cards)
        if self.hand_type == __value.hand_type:
            for my_card, their_card in zip(self.cards, __value.cards):
                if my_card < their_card:
                    # print(f"MY CARD {my_card} < THEIR CARD {their_card}")
                    return True
                elif my_card > their_card:
                    return False
            return False
        else:
            return self.hand_type.value < __value.hand_type.value


def main():
    lines = read_lines("7_1/input.txt", rstrip=True)
    # lines = read_lines("7_2/test_input.txt", rstrip=True)
    hands: list[Hand] = []
    for line in lines:
        hand = Hand(*line.split())
        hands.append(hand)
    hands.sort()
    res = 0
    for i, hand in enumerate(hands):
        res += (i + 1) * hand.bid
    print(res)

if __name__ == "__main__":
    main()
