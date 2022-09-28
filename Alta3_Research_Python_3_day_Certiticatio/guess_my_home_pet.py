#!/usr/bin/env python3
""" Author:  Anthony Murguia 
    Purpose: Interactive program to guess the kind of pet I have""" 

def main():
    """ Main program """
    round = 0                                    # integer initiated to zero
    while True:                                  # sets infinite loop condition
        round = round + 1                        # Increase the round counter
        print("What kind of pet do you think I have? ")
        answer = input("you guess---> ")         # string of answer collected
        if answer == 'dog':                      # Logic to check if correct answer
            print('WOW! You are correct!')
            break                                # Break statement exit the while loop 
        elif answer == 'DOG':                    # All CAPS string 
            print('WOW! You are correct!')       # Logic check
            break                                # Break statement exit the while loop
        elif answer == 'Dog':                    # Captial first letter of correct answer
            print('WOW! You are correct!')       # Logic check
            break                                # Break statement exit the while loop
        elif round == 3:                         # Last chance to guess
            print('Sorry, the answer is dog.')   # If entered wrong answer 
            break                                # Break statemnet, exit loop
        else:                                    # If wrong answer is not equal to 3, continue 
            print('Not quite, try again!')        
main()
