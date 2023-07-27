
import random


suits = ('Hearts', 'Diamonds', 'Spades', 'Clubs')
ranks = ('Two', 'Three', 'Four', 'Five', 'Six', 'Seven', 'Eight', 'Nine', 'Ten', 'Jack', 'Queen', 'King', 'Ace')
values = {'Two':2, 'Three':3, 'Four':4, 'Five':5, 'Six':6, 'Seven':7, 'Eight':8, 
            'Nine':9, 'Ten':10, 'Jack':10, 'Queen':10, 'King':10, 'Ace':True}


class Card:
    
    def __init__(self,suit,rank):
        self.suit = suit
        self.rank = rank
        self.value = values[rank]
        
    def __str__(self):
        return self.rank + ' of ' + self.suit
    

class Deck:
    
    def __init__(self):
        self.all_cards = [] 
        for suit in suits:
            for rank in ranks:
                self.all_cards.append(Card(suit,rank))
                
    def shuffle(self):
        random.shuffle(self.all_cards)
        
    def deal_one(self):
        return self.all_cards.pop() 
    

class Human:
    
    def __init__(self):
        self.cards = []

    def hold(self,card):
        self.cards.append(card)
    
    def count_cards(self):

        def two_int_val(one,two,total):
            val_one = one + total
            val_two = two + total

            if (21 - val_one > 0) and (21 - val_two > 0):
                if val_one > val_two:
                    return val_two
                else:
                    return val_one
            elif (21 - val_one > 0) and (21 - val_two < 0):
                return val_two
            elif (21 - val_one < 0) and (21 - val_two > 0):
                return val_one
            elif (21 - val_one < 0) and (21 - val_two < 0):
                if val_one > val_two:
                    return val_one
                else:
                    return val_two

        self.theres_ace = False
        self.num_of_aces = 0
        self.total_value = 0

        for card in self.cards:
            if (card.rank == 'Ace'):
                self.theres_ace = True
                self.num_of_aces += 1
                continue

            self.total_value += values[card.rank]
        
        print("you total value of cards now is: ", self.total_value)

        while self.theres_ace:
            if (self.num_of_aces == 1):
                return two_int_val(1,11,self.total_value)
            elif (self.num_of_aces == 2):
                return two_int_val(2,12,self.total_value)
            elif (self.num_of_aces == 3):
                return two_int_val(3,13,self.total_value)
            elif (self.num_of_aces == 4):
                return two_int_val(4,14,self.total_value)
        
        print(f"The total value of the dealer's cards are {self.total_value}.")

        return self.total_value
         

class Player(Human):
    
    def __init__(self,name):
        super().__init__()
        self.name = name
        self.cash = 500

    def count_cards(self):
        self.theres_ace = False
        self.num_of_aces = 0
        self.total_value = 0

        for card in self.cards:
            if (card.rank == 'Ace'):
                self.theres_ace = True
                self.num_of_aces += 1
                continue

            self.total_value += values[card.rank]
        
        while self.theres_ace:
            self.val_aces = int(input(f"You hold {self.num_of_aces} aces. Pick the total values you'd like to have for the aces/s."))
            if (self.num_of_aces == 1):
                if self.val_aces in [1,11]:
                    self.total_value += self.val_aces
                    self.theres_ace = False
                else:
                    print("You have selected the wrong total value. Try again.")
            elif (self.num_of_aces == 2):
                if self.val_aces in [2,12]:
                    self.total_value += self.val_aces
                    self.theres_ace = False
                else:
                    print("You have selected the wrong total value. Try again.")
            elif (self.num_of_aces == 3):
                if self.val_aces in [3,13]:
                    self.total_value += self.val_aces
                    self.theres_ace = False
                else:
                    print("You have selected the wrong total value. Try again.")
            elif (self.num_of_aces == 4):
                if self.val_aces in [4,14]:
                    self.total_value += self.val_aces
                    self.theres_ace = False
                else:
                    print("You have selected the wrong total value. Try again.")
        
        print(f"The total value for your cards are {self.total_value}.")
        
        return self.total_value
    
    def __str__(self):
        print(f"I,{self.name} have ${self.cash}!")
    

class Dealer(Human):
    
    def d_speak(wl,player,value):
        if wl:
            print(f"You,{player} have won ${value}.")
        else:
            print(f"You,{player} have lost ${value}.")


round_num = 0
game_status = True

while game_status:

    round_num+= 1

    if (round_num == 1):
        p1_name = input("Good Day. What is your name?")
        p1 = Player(p1_name)
        dealer = Dealer()
        print(f"Good Day {p1_name}. We shall now start the game of blackjack.")
        print("You will start with $500 and the payout for this game is 3/2. So you will win $3 for every $2 you bet.")
        print("Let us start the game now. Have fun playing.")
    
    print("You have $", p1.cash)
    pot = int(input("How much money would you like to bet?"))
    while pot > p1.cash:
        ans = input("You cannot bet this much money here as you don't have enough money. Press 'Y' to bet a lower amount or 'N' to exit the game.")
        if ans == 'Y':
            pot = int(input("How much money would you like to bet?"))
        elif ans == 'N':
            game_status = False
            break
        else:
            print("You entered a wrong amount please try again.")
    print("You are bettting: ",pot)
        
    
    deck = Deck()
    deck.shuffle()

    for i in range(4):
        if i == 3:
            dealer.cards.append(deck.deal_one())
            break

        if i == 2:
            d = deck.deal_one()
            dealer.cards.append(c)
            print("Card for dealer:",d)
            continue

        c = deck.deal_one()
        p1.cards.append(c)
        print("Card for player:",c)

    game_not_end = True

    while True:
        p1.count_cards()
        ans1 = input("Press 'Y' to hit or 'N' to stand.")        
        
        if ans1 == 'Y':
            c = deck.deal_one()
            p1.cards.append(c)
            print("Card for player:",c)
            p1.count_cards()

            if p1.total_value > 21:
                print("Player has gone over 21. Player has lost.")
                dealer.d_speak(False,p1,pot)
                p1.cash -= pot
                print(p1)
                game_not_end = False
                break
        elif ans1 == 'N':
            break
        else:
            print("You entered a wrong amount please try again.")
    
    print("The dealer's second card is:",dealer.cards[1])

    while game_not_end:
        dealer.count_cards()
        if dealer.total_value > 21:
                print("Dealer has gone over 21. Dealer has lost.")
                dealer.d_speak(True,p1,pot)
                p1.cash += pot
                print(p1)   
                game_not_end = False
                break    
        
        if dealer.total_value  <= p1.total_value:
            c = deck.deal_one()
            dealer.cards.append(c)
            print("Card for player:",c)
            dealer.count_cards()

        else:
            print("Dealer is closer to 21 than Player. Dealer has won")
            dealer.d_speak(False,p1,pot)
            p1.cash -= pot
            print(p1)
            game_not_end = False
    
    while True:
        ans2 = input("Press 'Y' to keep on playing and 'N' to stop playing this game")

        if ans2 == 'Y':
            break
        elif ans1 == 'N':
            game_status = False
            break
        else:
            print("You entered a different thing than asked. Please try again.")
        
    






