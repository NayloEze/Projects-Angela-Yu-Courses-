rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

#Write your code below this line 👇
import random
game_images = [rock,paper,scissors]
rock_paper_scissors = int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors:  "))
if rock_paper_scissors >= 3 or rock_paper_scissors < 0:
    print("Wrong attempt, try again")
else:
    print(game_images[rock_paper_scissors])
    
    computer_random_choice = random.randint(0,2)
    print(f"Computer enters: {computer_random_choice}")
    print(game_images[computer_random_choice])


    if rock_paper_scissors == 0 and computer_random_choice == 2:
        print(" You win the game ")
    elif rock_paper_scissors == 2 and computer_random_choice == 0:
        print(" You lose") 
    elif rock_paper_scissors == 2 and computer_random_choice == 1:
        print(" You win the game ")
    elif rock_paper_scissors == 1 and computer_random_choice == 2:
        print(" You lose ")
    elif rock_paper_scissors == 1 and computer_random_choice == 0:
        print(" You win the game ")
    elif rock_paper_scissors == 0 and computer_random_choice == 1:
        print(" You lose ")
    elif rock_paper_scissors == computer_random_choice:
        print( "It's a draw, try again" )
