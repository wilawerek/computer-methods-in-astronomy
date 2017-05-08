#!/bin/usr/python
# Emil Wilawer 2016-11-27
import random
import os
from numpy import fabs

#
# Klasy
#
class Card():
    deck=[]
    colors = ['karo','kier','pik','trefl']
    card_values = {11:['WALET',2], 12:['DAMA',3], 13:['KROL',4], 1:['AS',11]}
    card_values.update({x:[x,x] for x in range(2, 11)})

    def __init__(self, figure, color, points):
        self.figure = figure
        self.color = color
        self.points = points

    @staticmethod
    def new_deck():
        '''
        Create a new deck of cards
        '''
        for figure in range(1,14):
            for color in Card.colors:
                Card.deck.append(Card(Card.card_values[figure][0], color, Card.card_values[figure][1]))
        random.shuffle(Card.deck)
        return Card.deck

class Player():
    
    def __init__(self, name, hand, points=0):
        self.name = name
        self.hand = hand
        self.points = points
        
    def hit_me(self):
        self.hand.append(str(Card.deck[0].figure)+" "+Card.deck[0].color)
        self.total_pts()
        del Card.deck[0]

    def total_pts(self):
        self.points += int(Card.deck[0].points)
#-----------------------------------------------------------------------

# New Deck
Card.new_deck()

# Players
player1 = Player("Gracz", [])
player2 = Player("Komputer", [])

# Gameplay CPU
while player2.points <21:
    player2.hit_me()
# Gameplay player
print player1.name, player1.hand
print 'punkty: ', player1.points
while True:
    do = raw_input("\nCO ROBISZ?\nwcisnij ENTER aby dobrac karte\nnapisz \"stop\" aby zakonczyc\n")
    os.system('clear')

    if do=='stop':
        break
    else:
        player1.hit_me()
        print player1.name, player1.hand
        print 'punkty: ',player1.points
# Endgame
if fabs(21-player1.points) > fabs(21-player2.points):
    print '   PRZEGRANA\nGracz:    {}\nKomputer: {}'.format(player1.points, player2.points)
elif fabs(21-player1.points) < fabs(21-player2.points):
    print '     WYGRANA\nGracz:    {}\nKomputer: {}'.format(player1.points, player2.points)
else:
    print '       REMIS\nGracz:    {}\nKomputer: {}'.format(player1.points, player2.points)

