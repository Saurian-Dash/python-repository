from random import shuffle

class Card:

  def __init__(self, value, suit):

    self.suit = suit
    self.value = value

  def __repr__(self):

    return '{} of {}'.format(self.value, self.suit)

class Deck:

  def __init__(self):

    suits = ['Hearts', 'Diamonds', 'Clubs', 'Spades']
    values = ['A','2','3','4','5','6','7','8','9','10','J','Q','K']
    self.cards = [Card(value, suit) for suit in suits for value in values]
    print(self.cards)

  def __repr__(self):

    return 'Deck of {} cards'.format(self.count())

  def _deal(self, n):

    count = self.count()
    actual = min([count, n])
    if count == 0:
      raise ValueError('All cards have been dealt!')
    cards = [self.cards.pop(-x) for x in range(0, n)]
    print('{} cards have been dealt: {}'.format(actual, cards))
    self.count()

    return cards

  def deal_card(self):

    return self._deal(1)[0]

  def deal_hand(self, n):

    return self._deal(n)

  def count(self):

    count = len(self.cards)
    print('{} cards remaining'.format(count))

    return count

  def shuffle(self):
      
    if self.count() < 52:
      raise ValueError('Only full decks can be shuffled!')
    print('\nShuffling cards...')
    shuffle(self.cards)
