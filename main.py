from art import logo 
import random
def clear_console():
    print("\033[H\033[J")

cards = [11,2,3,4,5,6,7,8,9,10,10,10,10] # create a card list
play_again = True

while play_again:
    choice = input("Do you want to play a game of blackjack? type 'y' to start, or 'n' to leave: ")
    if choice == 'y':
        clear_console()
        
        #1st round: player and computer each get two random cards.
        print(logo)
        selected_cards = random.sample(cards, k=2) #randomly select two cards for player
        total_value = sum(selected_cards)  # add up player's two cards
        computer_firstCard = sum(random.sample(cards,k=1)) 

        print(f"   Your cards: {selected_cards}, your current score: {total_value}.\n")
        print(f"   Computer's first card: {computer_firstCard}\n")
        
        # update computer card list
        computer_second_card = sum(random.sample(cards, k=1))                
        computer_Cards = [computer_firstCard,computer_second_card]
        computer_total_value = sum(computer_Cards) # add up computer's two cards
       
        # check if has blackjack
        if computer_total_value == 21:  # computer has blackjack
            print(f"   Your final hand: {selected_cards}, final score: {total_value}\n")
            print(f"   Computer's final hand: {computer_Cards}, final score: 0\n")
            print(f"Lose, oppent has Blackhack 🙀")
            play_again = False

        elif computer_total_value == total_value == 21: # both have blackjacks
            print(f"   Your final hand: {selected_cards}, final score: {total_value}\n")
            print(f"   Computer's final hand: {computer_Cards}, final score: 0\n")
            print("Win Win! Both BlackJacks!!!")
            play_again = False

        elif total_value == 21: # player has blackjack
            print(f"   Your final hand: {selected_cards}, final score: {total_value}\n")
            print(f"   Computer's final hand: {computer_Cards}, final score: 0\n")
            print("You Win! BlackJack!!!")
            play_again = False
        
        # check if player's score over 21:
        if total_value > 21:
            print(f"   You final hand: {selected_cards}, final score: {total_value}.\n")
            print(f"   Computer's final hand: {computer_Cards}, final score: {computer_total_value}\n")
            print("You went over. You lose 😢😢😢\n")
            play_again = False
        #check if player want to get another card
        
        if total_value < 21:
            should_continue = input("Type 'y' to get another card, type 'n' to pass: ")
            print()    
        # player choice of choosing 'y' or 'n':
            if should_continue == "y":  
                    select_another_card = sum(random.sample(cards, k=1)) #randomly one more card for player
                    total_value += select_another_card
                    selected_cards.append(select_another_card)

                    if total_value == 21:
                        print(f"   You final hand: {selected_cards}, final score: {total_value}.\n")
                        print(f"   Computer's final hand: {computer_Cards}, final score: {computer_total_value}\n")
                        print("BlackJack! You win! 🎭")
                        
                    elif total_value > 21:
                        print(f"   You final hand: {selected_cards}, final score: {total_value}.\n")
                        print(f"   Computer's final hand: {computer_Cards}, final score: {computer_total_value}\n")
                        print("You went over. You lose 🤦🏼\n") 
                        
                # update player cars list. 
                # When player cards less than 21, they can keep choosing to get another card.
                #? where to put this while loop?
                    else:
                        print(f"   You cards: {selected_cards}, current score: {total_value}.\n")
                        print(f"   Computer's first card: {computer_firstCard}\n")
                        # add the new card to the list
                        
                        
            else: 
                #if computer cards less than 17, it must continueto choose card until it over 17.
                #while loop to do it:
                while computer_total_value < 17:
                    computer_next_Card = sum(random.sample(cards, k=1))
                    computer_total_value += computer_next_Card
                    # update computer_Cards list:
                    computer_Cards.append(computer_next_Card)
                print(f"   Your final hand: {selected_cards}, final score: {total_value}.\n")
                print(f"   Computer's final hand: {computer_Cards}, final score: {computer_total_value}\n")
                # compare final hand score, whose score closet to 21 is the winner
                if total_value > computer_total_value:
                    print("You win 👍🎸")
                    
                elif computer_total_value >21:
                    print("You win 👍")
                    
                elif total_value < computer_total_value:
                    print("You lose 😢")
                    
                else:
                    print(" Draw 🤝")
                    
  
    else:
        play_again = False 
          
clear_console()        
    