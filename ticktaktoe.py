def drawBoard(board):
	print(board['top-L']+'|'+board['top-M']+'|'+board['top-R'])
	print("-+-+-")
	print(board['mid-L']+'|'+board['mid-M']+'|'+board['mid-R'])
	print("-+-+-")
	print(board['bot-L']+'|'+board['bot-M']+'|'+board['bot-R'])
	
theBoard = {'top-L':' ', 'top-M':' ', 'top-R':' ',
			'mid-L':' ', 'mid-M':' ', 'mid-R':' ',
			'bot-L':' ', 'bot-M':' ', 'bot-R':' '}	

turn = 'X'
for i in range(9):
	drawBoard(theBoard)
	print("The turn for "+ turn +". Which move do you want? ")
	move = input()
	theBoard[move] = turn
	if turn == 'X':
		turn = 'O'
	else:
		turn = 'X'

drawBoard(theBoard)
