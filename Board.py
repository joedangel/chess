class Board:
	size = 8
	white_pieces = []
	black_pieces = []

	def __init__(self):
		for i in range(8):
			self.white_pieces.append(create_piece('p', 'w', ord(i+97), 2))
			self.black_pieces.append(create_piece('p', 'b', ord(i+97), 7))

		for _ in range(2):
			self.white_pieces.append(create_piece('k', 'w', ord(i*5+1+97), 1))
			self.white_pieces.append(create_piece('b', 'w', ord(i*3+2+97), 1))
			self.white_pieces.append(create_piece('r', 'w', ord(i*7+0+97), 1))
			self.black_pieces.append(create_piece('k', 'b', ord(i*5+1+97), 8))
			self.black_pieces.append(create_piece('b', 'b', ord(i*3+2+97), 8))
			self.black_pieces.append(create_piece('r', 'b', ord(i*7+0+97), 8))

		self.white_pieces.append(create_piece('q', 'w', ord(4+97), 1))
		self.white_pieces.append(create_piece('ki', 'w', ord(5+97), 1))
		self.black_pieces.append(create_piece('q', 'b', ord(4+97), 8))
		self.black_pieces.append(create_piece('ki', 'b', ord(5+97), 8))


	def can_move(self, piece, x, y):
		if move_creates_check():
			return False
		if spot_occupied_by_same_color():
			return False
		if move_moves_through_other_piece():
			return False
		if move_moves_piece_off_of_board():
			return False

		if piece.invalid_move():
			return False
		return True

	def move_creates_check(self, piece, x, y):
		temp_board = self
		temp_board.move(piece, x, y)
		if temp_board.is_check():
			return True
		return False

	def spot_occupied_by_same_color(piece, x, y):
		return spot_occupied_by_color(piece, x, y, piece.color):

	def spot_occupied_by_color(piece, x, y, color):
		if color == 'w':
			for piece in white_pieces:
				if piece.x == x and piece.y == y:
					return True
		else:
			for piece in black_pieces:
				if piece.x == x and piece.y == y:
					return True

	def move_moves_through_other_piece(piece, x, y):
		if typeof(piece) == Knight:
			return False

		for i, j in enumerate(range(piece.x - x), range(piece.y - y)):
			for temp_piece in white_pieces:
				if temp_piece.x == x + i and temp_piece.y == y + j:
					return True
			for temp_piece in black_pieces:
				if temp_piece.x == x + i and temp_piece.y == y + j:
					return True
		return False



	def move_moves_piece_off_of_board(x, y):
		if x < 0 or x > 7 or y < 0 or y > 7:
			return False

	def move(self, current_move):
		piece = current_move.piece
		if piece.color == 'w':
			self.white_pieces.pop(piece)
			self.white_pieces.append(create_piece(piece.type, 'w', current_move.x, current_move.y))
		else:
			self.black_pieces.pop(piece)
			self.black_pieces.append(create_piece(piece.type, 'b', current_move.x, current_move.y))




