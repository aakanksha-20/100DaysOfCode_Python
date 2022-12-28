#Day 11: Blackjack - Capstone project 

import random
from art import logo
import os 

def deal_card():
    """Returns a random card from the deck."""
    cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    card = random.choice(cards)
    return card

def calculate_score(cards):
    """Take a list of cards and return the score calculated from the cards"""
    #0 represents the presence of a blackjack in our game
    if sum(cards) == 21 and len(cards) == 2:
        return 0
    if 11 in cards and sum(cards) > 21:
        cards.remove(11)
        cards.append(1)
    return sum(cards)

def compare(user_score, computer_score):
    #Bug fix. If you and the computer are both over, you lose.
    if user_score > 21 and computer_score > 21:
        return "\nYou went over. You lose :("
    if user_score == computer_score:
        return "\nIt's a Draw. :/"
    elif computer_score == 0:
        return "\nOpponent has Blackjack. You Lose. :("
    elif user_score == 0:
        return "\nWin with a Blackjack! "
    elif user_score > 21:
        return "\nYou went over. You lose :/"
    elif computer_score > 21:
        return "\nOpponent went over. You win :D"
    elif user_score > computer_score:
        return "\nYou win :D"
    else:
        return "\nYou lose :("

def blackjack():
    print(logo)
    
    user_cards = []
    computer_cards = []
    #Flag
    game_over = False

    #Will loop through and assign to random cards and append them to the empty lists
    for i in range(2):
        user_cards.append(deal_card())
        computer_cards.append(deal_card())


    while not game_over:
        #The score will need to be rechecked with every new card drawn
        user_score = calculate_score(user_cards)
        computer_score = calculate_score(computer_cards)
        print(f"\n\n---Your cards: {user_cards}, current score: {user_score}")
        print(f"---Computer's first card: {computer_cards[0]}")

        if user_score == 0 or computer_score == 0 or user_score > 21:
            game_over = True
        else:
        #The game does not end
        #Hence, user can draw another card, or not (then, the game ends)
            user_should_deal = input("Type 'y' to get another card, type 'n' to pass: ")
        if user_should_deal == "y":
            user_cards.append(deal_card())
        else:
            game_over = True

    #After the user is done, then the computer plays
    while computer_score != 0 and computer_score < 17:
        computer_cards.append(deal_card())
        computer_score = calculate_score(computer_cards)

    print(f"\n\n---Your final hand: {user_cards}, final score: {user_score}")
    print(f"---Computer's final hand: {computer_cards}, final score: {computer_score}")
    print(compare(user_score, computer_score))


print("\n\n __________Our Blackjack House Rules__________")
print(" -> The deck is unlimited in size.") 
print(" -> There are no jokers. ")
print(" -> The Jack/Queen/King all count as 10.")
print(" -> The the Ace can count as 11 or 1.")
print(" -> All the cards have equal probability of being drawn.")
print(" -> The computer is the dealer.")
print(" \n     Let's Play! ")

while input("\nDo you want to play a game of Blackjack? Type 'y' or 'n': ") == "y":
    os.system('clear')
    blackjack()
