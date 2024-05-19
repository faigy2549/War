from Deck import Deck
from Player import Player
deck = Deck()
print(deck)
deck.mix()

p1 = Player(input('enter name'), [])
p2 = Player(input('enter name'), [])
for k in range(0, 26):
    p1.pile += [deck.turn()]
    p2.pile += [deck.turn()]
print("➖➖➖➖➖➖➖➖➖➖➖➖")


def equal(a1 , b2,a,b):
    if len(p2.pile) < 4:
        p2.pile = []
        return

    elif len(p1.pile) < 4:
        p1.pile = []
        return

    x1 = p1.pickcard()
    x2 = p1.pickcard()
    x3 = p1.pickcard()
    x4 = p1.pickcard()
    print(f'war card: ')
    p1.printpcard(x4)
    y1 = p2.pickcard()
    y2 = p2.pickcard()
    y3 = p2.pickcard()
    y4 = p2.pickcard()
    print(f'war card: ')
    p2.printpcard(y4)
    if x4.cardValue > y4.cardValue:
        a += [a1, x1, x2, x3, x4]
        b += [b2, y1, y2, y3, y4]
        p1.addcard(a)
        p1.addcard(b)
        print(f' {p1.name} beat {p2.name}!!!')
        print()
    elif x4.cardValue < y4.cardValue:
        a += [a1, x1, x2, x3, x4]
        b += [b2, y1, y2, y3, y4]
        p2.addcard(a)
        p2.addcard(b)
        print(f'{p2.name} beat {p1.name}!!!')
        print()
    else:
        a += [a1,x1, x2, x3,x4]
        b += [b2,y1, y2, y3,y4]
        print('💥💥💥💥💥💥💥💥💥💥💥💥💥💥💥💥💥💥💥💥💥💥💥💥💥💥💥💥💥💥💥💥💥💥💥💥💥💥💥💥💥💥💥💥💥💥💥💥💥💥💥💥💥💥💥💥💥💥💥')
        equal(x4, y4,a,b)
count=0;
while p1.pile!=[] and p2.pile!=[] and count<1000:
    p1.printplayer()
    p2.printplayer()
    a1 = p1.pickcard()
    p1.printpcard(a1)
    b2 = p2.pickcard()
    p2.printpcard(b2)
    count+=1
    if a1.cardValue == b2.cardValue:
        print('WAR TIME!')
        equal(a1, b2,[],[])
    elif a1.cardValue > b2.cardValue:
        p1.addcard([a1 , b2])
    elif a1.cardValue < b2.cardValue:
        p2.addcard([a1 , b2])





if len(p1.pile) >1:
    print(f'player {p1.name} winner!!!!!😀🤣🤣😍😘❤❤👍👍')
else:
    print(f'player {p2.name} winner!!!!!😀🤣🤣😍😘❤❤👍👍')


