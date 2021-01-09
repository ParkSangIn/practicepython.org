while True:
	player1 = input("player1 - Enter Rock Scissors Paper : ")
	player2 = input("player2 - Enter Rock Scissors Paper : ")

	if player1 == 'Rock':
		if player2 == 'Rock':
			print("Draw")
		elif player2 == 'Scissors':
			print("player1 win!")
		else:
			print("player2 win!")
	elif player1 == 'Scissors':
		if player2 == 'Rock':
			print("player2 win!")
		elif player2 == 'Scissors':
			print("Draw")
		else:
			print("player1 win!")
	else:
		if player2 == 'Rock':
			print("player1 win!")
		elif player2 == 'Scissors':
			print("player2 win!")
		else:
			print("Draw")

	answer = input("Do you want to play more ? (y/n) : ")
	if answer == 'n':
		print("Thank you for playing~ good bye!")
		break
	else:
		print("OK! Next round~ start!")
