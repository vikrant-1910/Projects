import random

title= ("Welcome to Rock,paper and Scissor Game")

print(title)

game_list=['rock','paper','scissor']

flag=True
while flag:
    user=input("Enter your choice:")
    computer= random.choice(game_list)

    print("User:",user)
    print("Computer:",computer)

    for i in range(1,6):
        if user==computer:
            print("Match Tie")
        elif computer=='rock' and user=='scissor' or computer=='scissor' and user=='paper' or computer=='paper' and user=='rock':
            print("Computer won")    
        elif user=='rock' and computer=='scissor' or user=='scissor' and computer=='paper' or user=='paper'and computer=='rock':
            print("User won")

    choice=input("Do you want to continue if yes press y if no press n:")
    if choice=='y' or choice=='yes':
        flag=True
    else:
        flag=False
