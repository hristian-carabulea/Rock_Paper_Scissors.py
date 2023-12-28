import random
################## Game Rules #####################################
# https://en.wikipedia.org/wiki/Rock_paper_scissors
#
# rock beats scissors
# scissors beats paper
# paper beats rock
#
# choices = ["rock","paper","scissors"]
choices = ["r","p","s"]
player = None
computer_score = 0
player_score = 0
tie_score = 0

while True and player != "q": # keep playing until player choose to quit
   
    computer = random.choice(choices)
    player = None
    while player not in choices and player != "q":
        player = input("(r)ock, (p)aper, (s)cissors, or (q)uit : ").lower()

    if player == "":
        player = " " # change nothing to character to prevent error
    if player[0] == "q": # quit
        print("Game ended!")
        break
    else:
        if player == computer: # if the same choices
            print('Player: ', player[0])
            print("Computer: ", computer[0])
            print("### TIE! ###")
            tie_score += 1
        elif player == "r": # rock
            if computer == "p": # paper # paper beats rock
                print('Player: ', player[0])
                print("Computer: ", computer[0])
                print("## Paper beats rock! YOU LOSE! ##")
                computer_score += 1
            if computer == "s": # scissors # rock beats scissors
                print('Player: ', player[0])
                print("Computer: ", computer[0])
                print("## Rock beats scissors. YOU WIN! ##")
                player_score += 1
        elif player == "r": # rock
            if computer == "p": # paper beats rock
                print('Player: ', player[0])
                print("Computer: ", computer[0])
                print("## YOU LOSE! ##")
                computer_score += 1
            if computer == "s": # scissors # rock beats scissors
                print('Player: ', player[0])
                print("Computer: ", computer[0])
                print("## YOU WIN! ##")
                player_score += 1
        elif player == "s": # scissors
            if computer == "r": # rock # rock beats scissors
                print('Player: ', player[0])
                print("Computer: ", computer[0])
                print("## YOU LOSE! ##")
                computer_score += 1
            if computer == "p": # paper # scissors beats paper
                print('Player: ', player[0])
                print("Computer: ", computer[0])
                print("## YOU WIN! ##")
                player_score += 1
        elif player == "p": # paper
            if computer == "s": # scissors # scissors beats paper
                print('Player: ', player[0])
                print("Computer: ", computer[0])
                print("## YOU LOSE! ##")
                computer_score += 1
            if computer == "r": # rock # paper beats rock
                print('Player: ', player[0])
                print("Computer: ", computer[0])
                print("## YOU WIN! ##")
                player_score += 1

print("######################")
print("Computer Score: ", computer_score)
print("Player Score:   ", player_score)
print("Number of ties: ", tie_score)
