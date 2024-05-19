class Card:
    def __init__(self, id, shape):
        self.id = id
        self.shape = shape
        self.cardValue = id
        if id == "j":
            self.cardValue = 11
        elif id == "q":
            self.cardValue = 12
        elif id == "k":
            self.cardValue = 13

    def __str__(self):
        print(f'{self.id} {self.shape}')

