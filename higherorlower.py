import random

class Card:
    
    #Represents a playing card with a suit and rank.
    suits = ["♠", "♥", "♦", "♣"]
    ranks = ["A", "2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K"]
   
    def __init__(self, suit, rank):

        if not (suit in Card.suits and rank in Card.ranks):
            raise ValueError("Invalid card: " + str(suit) + " " + str(rank))

        self.suit = suit
        self.rank = rank

    def __str__(self):
        return f"{self.rank}{self.suit}"

    def card_str(self):
        if self.rank == "10":
            return f"""
            ┌─────┐
            │10   │
            │  {self.suit}  │
            │   10│
            └─────┘
            """
        else:
            return f"""
            ┌─────┐
            │{self.rank}    │
            │  {self.suit}  │
            │    {self.rank}│
            └─────┘
            """
    def value(self):
        return Card.ranks.index(self.rank) + 1
    
class Deck:

    #Initializes a Deck object with a full deck of 52 cards.
    def __init__(self):
        self.cards = [Card(suit, rank) for suit in Card.suits for rank in Card.ranks]

    def shuffle(self):
        random.shuffle(self.cards)#shuffles the deck

    def debug_print_deck(self):
        for card in self.cards:
            print(card.card_str())
    
    def deal(self, num_cards = 1):
        print(self.cards.pop(0).card_str()) #pop removes the card from the deck whilst also letting it
deck = Deck() #defines the deck function
deck.shuffle() #shuffles the deck
deck.deal() #deals a single card from the deck
print(input("Is the next card higher or lower?"))
if Card.value > Card.value == higher:
    else Card.value < Card.value == lower


