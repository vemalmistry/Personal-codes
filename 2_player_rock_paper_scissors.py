more = "y"
while more == "y":
	p1 = input("Player 1. rock, paper, scissors: ")
	p2 = input("Player 2. rock, paper, scissors: ")
	if p1 == "rock" and p2 == "paper" or p1 == "paper" and p2 == "scissors" or p1 == "scissors" and p2 == "rock":
		print("Congratulations, Player 2 wins")
	elif p1 == "paper" and p2 == "rock" or p1 == "scissors" and p2 == "paper" or p1 == "rock" and p2 == "scissors":
		print("Congratulations, Player 1 wins")
	elif p1 == p2:
		print("Draw")
	else:
		print("You must select rock, paper or scissors")
	more = input("Do you wish to play again (y/n): ")
	if more == "n":
		print("Thanks for playing")
		break