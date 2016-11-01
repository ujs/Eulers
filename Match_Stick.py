# Matchstick game
# There are total 21 match sticks
# Game prompts user to enter a positive integer <= 4
# Computer also guesses a number <= 4 ( to win the computer should not start the game)
# To win, the computer should always guess such that Computer's guess = 5 - User's Guess
# Whoever picks the last matchstick loses

def match_game():
    
    print ("Welcome to matchstick game (you are playing against the computer. There are 21 matchsticks.You have to pick 1, 2, 3, or 4 matches when asked. Whoever picks the last match loses")
    total = 0
    while total <= 21:
       user_guess = int(input("Enter a positive integer <=4: "))
       total += user_guess
       if total >= 21:
           print ("User lost")
           break
       assert isinstance(user_guess, int) and user_guess <= 4
       computer_guess = 5-user_guess
       total += computer_guess
       if total >= 21:
           print ("Computer lost")
    return None



       
                               
