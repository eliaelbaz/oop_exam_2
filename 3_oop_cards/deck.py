import random
from functools import wraps
from card import Card
from enums import CardSuit, CardRank

class DeckCheatingError(Exception):
    def __init__(self, message: str):
        super().__init__(message)

def fair_deck(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        instance = args[0]

        result1 = func(*args, **kwargs)
        cards_after_first_shuffle = list(instance._cards)

        result2 = func(*args, **kwargs)
        cards_after_second_shuffle = list(instance._cards)

        if cards_after_first_shuffle == cards_after_second_shuffle:
            raise DeckCheatingError("Deck was not shuffled properly")

        return result1

    return wrapper

class Deck:
    def __init__(self, shuffle=True):
        self._cards = [Card(suit, rank) for suit in CardSuit for rank in CardRank]
        self._index = 0
        if shuffle:
            self.shuffle()

    @property
    def cards(self):
        return list(self._cards)

    @fair_deck
    def shuffle(self):
        random.shuffle(self._cards)
        return self._cards

    def draw(self):
        return self._cards.pop(0) if self._cards else None

    def add_card(self, card: Card):
        self._cards.append(card)

    def __len__(self):
        return len(self._cards)

    def __getitem__(self, index):
        return self._cards[index]

    def __iter__(self):
        self._index = 0
        return self

    def __next__(self):
        if self._index >= len(self._cards):
            raise StopIteration
        card = self._cards[self._index]
        self._index += 1
        return card
