
                                             # PROJECT 01 
                                        # SNAKE WATER GUN GAME
# ''' 
# SNAKE = 1
# WATER = -1 
# GUN = 0

# SNAKE > WATER
# WATER > GUN
# GUN > SNAKE

# '''
import random

game_dict = {"s" : 1 , "w" : -1 , "g" : 0}
reverse_game_dict = {1 : "snake" , -1 : "water" , 0 : "gun"}

your_choice = (input("enter your choice : "))
computer_choice = random.choice ([1 ,-1 , 0 ])
you = game_dict[your_choice]


print(f"you have chosen {reverse_game_dict[you]}, and computer has chosen {reverse_game_dict[computer_choice]}")

if (you  ==  computer_choice ):
    print("it's a draw") 
    
else: 

    if (computer_choice == 1 and you == -1):
        print("computer wins")
    elif (computer_choice == 1 and you == 0):
        print("you win")
    elif (computer_choice ==  -1 and you == 1):
        print("you win ")
    elif (computer_choice == -1 and you == 0):
        print("computer wins")
    elif (computer_choice == 0 and you == -1):
        print("you win")
    elif (computer_choice == 0 and you == 1):
        print("computer wins")

    else :
        print("something went wrong") 
















# # Import random module
# import random
# print('Snake - Water - Gun')


# # Input no. of rounds
# n = int(input('Enter number of rounds: '))


# # List containing Snake(s), Water(w), Gun(g)
# options = ['s', 'w', 'g']

# # Round numbers
# rounds = 1

# # Count of computer wins
# comp_win = 0

# # Count of player wins
# user_win = 0


# # There will be n rounds of game
# while rounds <= n:

# 	# Display round
# 	print(f"Round :{rounds}\nSnake - 's'\nWater - 'w'\nGun - 'g'")

# 	# Exception handling
# 	try:
# 		player = input("Choose your option: ")
# 	except EOFError as e:
# 		print(e)

# 	# Control of bad inputs
# 	if player != 's' and player != 'w' and player != 'g':
# 		print("Invalid input, try again\n")
# 		continue

# 	# random.choice() will randomly choose
# 	# item from list- options
# 	computer = random.choice(options)

# 	# Conditions based on the game rule
# 	if computer == 's':
# 		if player == 'w':
# 			comp_win += 1
# 		elif player == 'g':
# 			user_win += 1

# 	elif computer == 'w':
# 		if player == 'g':
# 			comp_win += 1
# 		elif player == 's':
# 			user_win += 1

# 	elif computer == 'g':
# 		if player == 's':
# 			comp_win += 1
# 		elif player == 'w':
# 			user_win += 1

# 	# Announce winner of every round
# 	if user_win > comp_win:
# 		print(f"You Won round {rounds}\n")
# 	elif comp_win > user_win:
# 		print(f"Computer Won round {rounds}\n")
# 	else:
# 		print("Draw!!\n")

# 	rounds += 1


# # Final winner based on the number of wons
# if user_win > comp_win:
# 	print("Congratulations!! You Won")
# elif comp_win > user_win:
# 	print("You lose!!")
# else:
# 	print("Match Draw!!")
