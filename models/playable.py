import random
from typing import List

import pydantic

class Card:
    __slots__ = ('value', 'suit')
    def __init__(self, value, suit):
        self.value = value
        self.suit = suit

    def __repr__(self):
        return f'{self.value}{self.suit}'

class Deck:
    suits = ['Hearts', 'Diamonds', 'Spades', 'Clubs']
    values = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A']
    def __init__(self):
        self.cards = [Card(suit=suit, value=value) for suit in self.suits for value in self.values]

    def shuffle(self):
        random.shuffle(self.cards)

    def draw(self, count=1):
        drawn = self.cards[:count]  # первые count карт
        self.cards = self.cards[count:]  # удаляем их из колоды
        return drawn if count > 1 else drawn[0]

    def __len__(self):
        return len(self.cards)

    def __repr__(self):
        return f'Deck({len(self.cards)} cards left)'


class Player:
    def __init__(self, name):
        self.name = name
        self.hand = []  # список карт на руках
        self.chips = 1000


    def receive(self, cards):
        if isinstance(cards, list):
            self.hand.extend(cards)
        else:
            self.hand.append(cards)

    def show_hand(self):
        return f"{self.name}'s hand: {', '.join(map(str, self.hand))}"

    def add_chips(self):
        self.chips = 1000

    def remove_chips(self, count):
        self.chips -= count

    def get_chips(self):
        return self.chips

    def __repr__(self):
        return {'name': self.name, 'chips': self.chips}

class Table:
    def __init__(self):
        self.cards : List[Card] = []
        self.deck : Deck = Deck()

    def add_cards(self, cards):
        if isinstance(cards, list):
            self.cards.extend(cards)
        else:
            self.cards.append(cards)

class Combination:
    def __init__(self, name, power, player):
        self.name = name
        self.power = power #high card - 100, pair - 200, double pair - 300, set - 400, street - 500, flash - 600, full house - 700,
        self.player = player #kare - 800, street flash - 900