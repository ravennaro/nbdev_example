# AUTOGENERATED! DO NOT EDIT! File to edit: ../nbs/01_deckc.ipynb.

# %% auto 0
__all__ = ['Deck', 'draw_n']

# %% ../nbs/01_deckc.ipynb 2
from .card import *
from fastcore.utils import *
import random

# %% ../nbs/01_deckc.ipynb 4
class Deck:
    "A deck of 52 cards, not including jokers"
    def __init__(self): 
        self.cards = [Card(s, r) for s in range(4) for r in range (1,14)]
    def __len__(self):
        return len(self.cards)
    def __str__(self): 
        return '; '.join(map(str, self.cards))
    def __contains__(self, card):
        return card in self.cards
    __repr__ = __str__
    def shuffle(self):
        "Shuffles the cards in this deck"
        random.shuffle(self.cards)

# %% ../nbs/01_deckc.ipynb 13
@patch
def pop(self:Deck,
        idx:int=-1): # The index of the card to remove, defaulting to the last one
    "Remove one card of the deck"
    return self.cards.pop(idx)

# %% ../nbs/01_deckc.ipynb 17
@patch
def remove(self:Deck,
           card: Card): # Card to remove
    "Removes 'card' from the deck or raises exception if is not there"
    self.cards.remove(card)

# %% ../nbs/01_deckc.ipynb 20
def draw_n(n:int, # number of cards to draw
           replace:bool=True): # whether pr not draw with replacement
    d = Deck()
    d.shuffle()
    if replace: return [d.cards[random.choise(range(len(d.cards)))] for _ in range (n)]
    else: return d.cards[:n]
