from deck import Deck, DeckCheatingError

deck = Deck()
print(f"Deck size: {len(deck)}")

try:
    deck.shuffle()
    print("Deck shuffled successfully")
except DeckCheatingError:
    print("Cheating detected Deck not shuffled properly")

card1 = deck.draw()
card2 = deck.draw()
print(f"Drawn cards: {card1}, {card2}")

print("\nIterating through all cards in the deck:")
for card in deck:
    print(card)