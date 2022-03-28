## Hi this Project implemented by Ahmad elnassag

############### Blackjack House Rules #####################

## The deck is unlimited in size. 
## There are no jokers. 
## The Jack/Queen/King all count as 10.
## The the Ace can count as 11 or 1.
## Use the following list as the deck of cards:
## cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
## The cards in the list have equal probability of being drawn.
## Cards are not removed from the deck as they are drawn.


import random
from art import logo
def Main_function():

    def deal_card():
        
        """return random cards"""
        
        cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
        card = random.choice(cards)
        return card
    
    def calc_score(cards):
        
        """return Score after cal and apply rules"""
        
        if sum(cards) == 21 and len(cards) == 2:
            return 0
        if 11 in cards and sum(cards) > 21:
            cards.remove(11)
            cards.append(1)
        return sum(cards)
    
    def compare(user_score, computer_score):
        
        """Compare Scores To Find Who Win !"""
        
        if user_score > 21 and computer_score > 21:
            return "You went over. You lose 😤"
        if user_score == computer_score:
            return "Draw 🙃"
        elif computer_score == 0:
            return "Lose, opponent has Blackjack 😱"
        elif user_score == 0:
            return "Win with a Blackjack 😎"
        elif user_score > 21:
            return "You went over. You lose 😭"
        elif computer_score > 21:
            return "Opponent went over. You win 😁"
        elif user_score > computer_score:
            return "You win 😃"
        else:
            return "You lose 😤"
   
    def play_game():
        
        """function make user interface"""
        
        print(logo)
        pc_cards = []
        user_cards = []
        game_over = False
        
        for _ in range(2):
            pc_cards.append(deal_card())
            user_cards.append(deal_card())

        while not game_over :
            pc_score = calc_score(pc_cards)
            user_score = calc_score(user_cards)
            
            print(f"   Your cards: {user_cards}, current score: {user_score}")
            print(f"   Computer's first card: {pc_cards[0]}")
            
            if pc_score == 0 or user_score == 0 or user_score > 21:
                game_over = True
            else:
                user_deal = input("Type 'y' to get another card, type 'n' to pass: ")
                if user_deal == "y":
                    user_cards.append(deal_card())
                else:
                    game_over = True
            while pc_score != 0 and pc_score < 17:
                pc_cards.append(deal_card())
                pc_score = calc_score(pc_cards)

            print(f"   Your final hand: {user_cards}, final score: {user_score}")
            print(f"   Computer's final hand: {pc_cards}, final score: {pc_score}")
            print(compare(user_score, pc_score))    
                
    while input("Hi I am Ahmad 😎.. Do you want to play a game of Blackjack? Type 'y' or 'n': ") == "y":
        play_game()

if __name__ == '__main__':
    Main_function()
    