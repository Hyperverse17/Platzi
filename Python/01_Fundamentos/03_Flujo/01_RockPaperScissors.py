
# Programa del juego priedra papel o tijeras

import random

def game(n):
    
    playerScore = 0
    cpuScore    = 0

    options = ["rock", "paper", "scissors"]
    
    for i in range(1,n+1):
        print("Round " + str(i))
        playerChoice = input("Player : ")
        cpuChoice    = random.choice(options)

        if playerChoice == "rock":
            if cpuChoice == "paper":
                cpuScore += 1
            elif cpuChoice == "scissors":
                playerScore += 1
            
        elif playerChoice == "paper":
            if cpuChoice == "scissors":
                cpuScore += 1
            elif cpuChoice == "rock":
                playerScore += 1

        elif playerChoice == "scissors":
            if cpuChoice == "rock":
                cpuScore += 1
            elif cpuChoice == "paper":
                playerScore += 1
        
        print("CPU    : "+ cpuChoice)
        print()

    print("--- Final Results ---")
    print("Player Score : " + str(playerScore))
    print("CPU Score    : " + str(cpuScore))
    print()
    if playerScore > cpuScore:
        print("You win!")
    elif playerScore < cpuScore:
        print("You loose...")
    elif playerScore == cpuScore:
        print("It's a tie")
    print()

game(5)