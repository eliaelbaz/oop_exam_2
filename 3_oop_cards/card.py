from enums import CardSuit, CardRank

class Card:
    def __init__(self, suit: CardSuit, rank: CardRank, face_up=True):
        self._suit = suit
        self._rank = rank
        self._face_up = face_up

    @property
    def suit(self):
        return self._suit

    @property
    def rank(self):
        return self._rank

    @property
    def face_up(self):
        return self._face_up

    def flip(self):
        self._face_up = not self._face_up
        return self._face_up

    def get_display_name(self):
        return f"{self._rank.name.capitalize()} of {self._suit.name.capitalize()}" if self._face_up else "?"

    def __eq__(self, other):
        return self._rank == other._rank and self._suit == other._suit

    def __lt__(self, other):
        return (self._rank, self._suit) < (other._rank, other._suit)

    def __gt__(self, other):
        return (self._rank, self._suit) > (other._rank, other._suit)

    def __hash__(self):
        return hash((self._suit, self._rank))

    def __str__(self):
        return self.get_display_name()

    def __repr__(self):
        return f"Card({self._suit}, {self._rank}, face_up={self._face_up})"