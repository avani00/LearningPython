'''
This is Blackjack game made using Python.
'''

import random


# creates lists for the suit, rank, and values of the ranks in a deck of cards.
SUITS = ['Hearts', 'Diamonds', 'Spades', 'Clubs']
RANKS = ['Two', 'Three', 'Four', 'Five', 'Six', 'Seven', 'Eight', 'Nine', 'Ten', 'Jack', 'Queen', 'King', 'Ace']
VALUES = {'Two':2, 'Three':3, 'Four':4, 'Five':5, 'Six':6, 'Seven':7, 'Eight':8, 'Nine':9, 'Ten':10, 'Jack':10, 'Queen':10, 'King':10, 'Ace':11}


PLAYING = True


class Card:
    '''
    Class for a card.
    '''

    def __init__(self, suit, rank):
        '''
        Creates a card.
        '''
        self.suit = suit
        self.rank = rank
        self.value = VALUES[rank]

    def __str__(self):
        '''
        Prints the card's information.
        '''
        return f'{self.rank} of {self.suit}'


class Deck:
    '''
    Class for a deck of cards.
    '''

    def __init__(self):
        '''
        Creates deck
        '''
        self.deck = []  # start with an empty list
        for suit in SUITS:
            for rank in RANKS:
                self.deck.append(Card(suit, rank)) # add each card one by one

    def __str__(self):
        '''
        Prints deck
        '''
        deck1 = []
        for card in self.deck:
            deck1.append(str(card))
        return str(deck1)

    def shuffle(self):
        '''
        Shuffles deck
        '''
        random.shuffle(self.deck)

    def deal(self):
        '''
        Deals card from the top of the deck
        '''
        card1 = self.deck[0]
        self.deck.pop(0)
        return card1


class Hand:
    '''
    Class for a hand in blackjack
    '''

    def __init__(self):
        '''
        Creates hand attributes
        '''
        self.cards = []  # start with an empty list as we did in the Deck class
        self.value = 0   # start with zero value
        self.aces = 0    # add an attribute to keep track of aces

    def add_card(self, card):
        '''
        Adds card to hand
        '''
        self.cards.append(card)
        if card.rank == 'Ace':
            self.aces += 1
        self.value += card.value

    def adjust_for_ace(self):
        '''
        Changes ace value if needed
        '''
        if self.value > 21 and self.aces > 0:
            self.aces -= 1
            self.value -= 10


class Chips:
    '''
    Chips (not the eating kind)
    '''

    def __init__(self):
        '''
        Creates chips
        '''
        self.total = 100  # This can be set to a default value or supplied by a user input
        self.bet = 0

    def win_bet(self):
        '''
        If they win the round
        '''
        self.total += self.bet

    def lose_bet(self):
        '''
        If they lose the round
        '''
        self.total -= self.bet


def take_bet():
    '''
    Takes a bet using user input
    '''

    while True:
        try:
            bet = int(input("What is your bet? "))
        except ValueError:
            print("That is not a valid bet amount.")
        else:
            if bet < 0:
                print("That is not a valid bet amount.")
            elif bet > player_chips.total:
                print("Unfortunately, you do not have enough chips to place this bet.")
            else:
                player_chips.bet = bet
                break


def hit(deck, hand):
    '''
    Adds card to hand when the player wants to hit
    '''

    card = deck.deal()
    hand.add_card(card)
    hand.adjust_for_ace()


def show_some(player, dealer):
    '''
    Shows one of the dealer's cards and all of the players cards
    '''

    print(f"Dealer's Cards: {dealer.cards[1]}")
    for card in player.cards:
        print(f"Player's Cards: {card}")
    print(f"Total Value: {player.value}")


def show_all(player, dealer):
    '''
    Shows all the dealer's and player's cards
    '''

    for card in player.cards:
        print(f"Player's Cards: {card}")
    print(f"Total Value: {player.value}")
    
    for card in dealer.cards:
        print(f"Dealer's Cards: {card}")
    print(f"Total Value: {dealer.value}")


def player_busts(player_chips):
    print(f"You have busted. You lose {player_chips.bet} chips") 
    player_chips.lose_bet()
    

def player_wins(player_chips):
    print(f"You win! You gain {player_chips.bet} chips")
    player_chips.win_bet()


def dealer_busts(player_chips):
    print(f"Dealer busts. You gain {player_chips.bet} chips")
    player_chips.win_bet()

    
def dealer_wins(player_chips):
    print(f"Dealer Wins. You lose {player_chips.bet} chips")
    player_chips.lose_bet()

    
def push():
    print("It's a push. You don't gain of lost anything.")

player_chips = Chips()
    
while PLAYING:
    # Print an opening statement
    print("Welcome to Blackjack!!! Please have fun and enjoy :]")

    # Create & shuffle the deck, deal two cards to each player
    deck = Deck()
    deck.shuffle()
    player_hand = Hand()
    dealer_hand = Hand()
    player_hand.add_card(deck.deal())
    dealer_hand.add_card(deck.deal())
    player_hand.add_card(deck.deal())
    dealer_hand.add_card(deck.deal())
        
    # Set up the Player's chips
    print(f"You have {player_chips.total} in total.")
    
    # Prompt the Player for their bet
    player_bet = take_bet()
    
    # Show cards (but keep one dealer card hidden)
    show_some(player_hand, dealer_hand)
    
    while True:
        
        # Prompt for Player to Hit or Stand
        choice = input("Do you want to hit or stand? ")
        if choice.capitalize() == 'Hit':
            hit(deck, player_hand)
            # Show cards (but keep one dealer card hidden)
            show_some(player_hand, dealer_hand)
            # If player's hand exceeds 21, run player_busts() and break out of loop
            if player_hand.value > 21:
                player_busts(player_chips)
                PLAYING = False
                break
        else:
            break

    if PLAYING:
        # If Player hasn't busted, play Dealer's hand until Dealer reaches 17
        while dealer_hand.value < 17 or dealer_hand.aces > 1:
            hit(deck, dealer_hand)
    
        # Show all cards
        show_all(player_hand, dealer_hand)
    
        # Run different winning scenarios
        if dealer_hand.value > 21:
            dealer_busts(player_chips)
        elif dealer_hand.value > player_hand.value:
            dealer_wins(player_chips)
        elif player_hand.value > dealer_hand.value:
            player_wins(player_chips)
        else:
            push()
    
    # Inform Player of their chips total 
    print(f"You have {player_chips.total} in total.")
    
    # Ask to play again
    playing_again = input("Do you wanna play again (say only 'Yes' or 'No'): ")
    if playing_again == 'Yes' or playing_again == 'yes':
        PLAYING = True
    else:
        PLAYING = False