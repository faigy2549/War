from Card import Card
from random import shuffle
class Deck:
    def __init__(self):
        self.cards = []
        shapes = ['♠', '♥', '♣', '♦']
        nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 'j', 'q', 'k']
        for i in shapes:
            for j in nums:
                self.cards.insert(0, Card(j, i))

    def mix(self ):
        return shuffle(self.cards)


    def turn(self):
        return self.cards.pop()





