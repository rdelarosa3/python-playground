board = [['__','__','__'],['__','__','__'],['__','__','__']]
marker = 'X'
winner = False

def reset_board():
	# global board
	global winner
	board = [['__','__','__'],['__','__','__'],['__','__','__']]
	return board

def display_board(board):
	print(board[0])
	print(board[1])
	print(board[2])

def set_marker():
	global marker
	marker = input("Player 1 pick X or O: ").upper()
	while marker != 'X' and marker !='O':
		set_marker()

def turn():
	global marker
	if marker == 'X':
		marker = 'O'
	else:
		marker  = 'X'
	return marker

def is_winner(board):
	global winner
	rowx = ['X','X','X']
	rowo = ['O','O','O']
	diag1 = [board[0][0], board[1][1], board[2][2]];
	diag2 = [board[0][2], board[1][1], board[2][0]];
	col1 = [board[0][2], board[0][1], board[0][0]];
	col2 = [board[1][2], board[1][1], board[1][0]];
	col3 = [board[2][2], board[2][1], board[2][0]];

	for i in board:
		if i == rowx or i == rowo:
			winner = True
	if diag1 == rowo:
		winner = True
	elif diag1 == rowx:
		winner = True
	elif diag2 == rowx:
		winner = True
	elif diag2 == rowo:
		winner = True
	elif col1 == rowx:
		winner = True
	elif col1 == rowo:
		winner = True
	elif col2 == rowx:
		winner = True
	elif col2 == rowo:
		winner = True
	elif col3 == rowx:
		winner = True
	elif col3 == rowo:
		winner = True				


def game_play():
	# ask player 1 to pick marker
	while True:	
		print('Player '+ marker + ' :')
		row = int(input('Please enter a row number: ')) - 1
		while row > 2 or row < 0:
			row = int(input('Please enter a row number: ')) - 1
		col = int(input('Please enter a col number: ')) -1
		while col > 2 or col < 0:
			col = int(input('Please enter a row number: ')) - 1
		if board[row][col] != 'X' and board[row][col] != 'O':
			board[row][col] = marker
			break 
	print('\n'*100)
	display_board(board)

	# check if player won
	is_winner(board)

	# if no winner check if tie or continue game
	if winner != True:
		if '__' not in [j for i in board for j in i]:
			reset_board()
			print("Draw")
			reply = input("Play Again: ").lower()
			while reply == None:
				reply = input("Play Again: ").lower()
			if reply == 'no':
				exit()
		turn()
		game_play()

	# if there is a winner congratulate or play again
	else:
		print(f'Player {marker} Wins!!')
		reset_board()
		reply = input("Play Again: ").lower()
		while reply == None:
			reply = input("Play Again: ").lower()
		if reply == 'yes':
			game_play()
		else:
			exit()

# actual game play
while not winner:
	print('Welcome To Py TicTacToe')
	display_board(board)
	set_marker()
	game_play()
