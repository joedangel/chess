class Loop:

	def __init__(self):
		self.board = Board()

	def make_move(self):
		possibleMoves = self.get_allowed_moves()
		best_move = None
		best_move_value = 0

		for move in possibleMoves:
			if self.get_move_value(move) > best_move_value:
				best_move_value = self.get_move_value(move)
				best_move = move

		self.board.move(best_move)

	def get_move_value(self, move):
		return 0

	def get_allowed_moves(self):
		possible_moves = self.get_possible_moves()
		allowed_moves = []
		
		for move in possible_moves:
			if self.board.can_move(move.piece, move.x, move.y):
				allowed_moves.append(move)

		return allowed_moves


	def get_possible_moves(self):
		# create moves
		moves = []
		for piece in self.board.white_pieces:
			for col in range(8):
				for row in range(8):
					moves.append(Move(piece, col, row))

		for piece in self.board.black_pieces:
			for col in range(8):
				for row in range(8):
					moves.append(Move(piece, col, row))
		return moves

	def print_board(self):
		for piece in self.board.white_pieces:
			print(piece)
		for piece in self.board.black_pieces:
			print(piece)

	def play(self):
		for _ in range(10):
			self.make_move()
			self.print_board()

