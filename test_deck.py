from Deck import Deck


deck = Deck()

for i in range(52):
    deck.__getitem__(i).print_card()

deck.shuffle()
for i in range(52):
    deck.__getitem__(i).print_card()

