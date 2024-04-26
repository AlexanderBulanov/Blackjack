""" 
File: blackjack_players.py
Author: Alexander Bulanov
"""

# Global Imports


# Local Imports #


### Defining Players for Tracking ###
class Player:
    def __init__(self):
        self.name = None # assign when new player is created
        self.is_dealer = False
        self.current_balance = None
        self.White = 0
        self.Pink = 0
        self.Red = 0
        self.Blue = 0
        self.Green = 0
        self.Black = 0
        self.Purple = 0
        self.Yellow = 0
        self.Brown = 0
        self.hole_card_face_down = False
        self.current_bet = []
        self.current_bet_value = None
        self.current_hands = []
        self.current_hand_scores = []
        self.action = None

    # Player actions are:
        # Out-of-Round:
            # Join
            # Leave
        # In-Round (Main Bets):
            # Place a Bet
            # Stand
            # Hit
            # Double-Down
            # Split
            # Surrender
        # In-Round (Side Bets):
            # Insurance
            # Even Money

    def create_casino_dealer():
        Dealer = Player()
        Dealer.name = 'Dealer'
        Dealer.is_dealer = True
        Dealer.current_balance = 10000
        Dealer.White = 1000
        Dealer.Pink = 1000
        Dealer.Red = 1000
        Dealer.Blue = 1000
        Dealer.Green = 1000
        Dealer.Black = 1000
        Dealer.Purple = 1000
        Dealer.Yellow = 1000
        Dealer.Brown = 1000
        Dealer.hole_card_face_down = True
        Dealer.current_bet = []
        Dealer.current_bet_value = None
        Dealer.current_hands = []
        Dealer.current_hand_scores = []
        Dealer.action = None
        return Dealer
    
    def create_new_player_from_template(player_name):
        NewPlayer = Player()
        NewPlayer.name = player_name
        NewPlayer.is_dealer = False
        NewPlayer.current_balance = 100
        NewPlayer.White = 50
        NewPlayer.Pink = 0
        NewPlayer.Red = 30
        NewPlayer.Blue = 20
        NewPlayer.Green = 4
        NewPlayer.Black = 0
        NewPlayer.Purple = 0
        NewPlayer.Yellow = 0
        NewPlayer.Brown = 0
        NewPlayer.hole_card_face_down = False
        NewPlayer.current_bet = []
        NewPlayer.current_bet_value = None
        NewPlayer.current_hands = []
        NewPlayer.current_hand_scores = []
        NewPlayer.action = None
        return NewPlayer
    
    def print_player_stats(self):
        print("*  *  *  *  *")
        if self.name == 'Dealer':
            print("Printing Dealer Statistics")
        else:
            print("Printing Statistics for Player '"+self.name+"'")
        for key, value in self.__dict__.items():
            if ((key == 'current_balance') or (key == 'current_bet_value')):
                print(str(key)+": $"+str(value))
            elif (key == 'current_hands') and (self.hole_card_face_down == True):
                hands = "["
                if (len(self.current_hands) == 0):
                    hands = hands+"]"
                else:
                    for hand in self.current_hands:
                        face_up_card = hand[0]
                        if (self.current_hands.index(hand) == (len(self.current_hands) - 1)):
                            hands = hands+"["+str(face_up_card)+", '**']]"
                        else:
                            hands = hands+"["+str(face_up_card)+", '**'], "
                # Print hole card as '**'
                print(str(key)+": "+hands)
            else:
                print(str(key)+": "+str(value))
        print("*  *  *  *  *")