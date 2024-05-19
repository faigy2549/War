#import Deck
class Player:
    def __init__(self, name,pile):
        self.name = name
        self.pile = pile
    def pickcard(self):
        return self.pile.pop()
    def addcard(self,a):
        if type(a) != list:
            a=[a]
        self.pile = a + self.pile


    def printplayer(self):
        print(f'Player:{self.name} has {len(self.pile)} cards')
    def printpcard(self,c):
        print(f'{self.name} picked {c.id} of {c.shape} ')
