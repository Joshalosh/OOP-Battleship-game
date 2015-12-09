from random import randint

class Board():
	
	def __init__(self):
		self.board = []
		for i in range(5):
			row1 = ['O' for i in range(5)]
			self.board.append(row1)
	
	def print_board(self):
		for i in self.board:
			print " ".join(i)
			
class Ship(Board):

	def random_row(self):
		return randint(0, len(self.board) - 1)
	
	def random_col(self):
		return randint(0, len(self.board[0]) -1)
		
class Win(Ship):
	
	def sink_ship(self):
		guess_row = int(raw_input("Guess Row: "))
		guess_col = int(raw_input("Guess Col: "))
		
		if guess_row == coord1 and guess_col == coord2:
			print "Congratulations! You sank my battleship!"
		else:
			if guess_row not in range(0, len(x.board) - 1) or \
			guess_col not in range(0, len(x.board[0]) - 1):
				print "Oops, that guess isn't even in the ocean, dumbass."
			else:
				print "You missed my battleship!"
				x.board[guess_row][guess_col] = "X"
				x.print_board()
		

x = Board()


ship1 = Ship()

coord1 = ship1.random_row()
coord2 = ship1.random_col()

print coord1
print coord2

x.print_board()

check = Win()

check.sink_ship()

