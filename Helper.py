def create_piece(type, color, col, row):
	if type == 'p':
		return Pawn(color, col, row)
	elif type == 'k':
		return Knight(color, col, row)
	elif type == 'b':
		return Bishop(color, col, row)
	elif type == 'r':
		return Rook(color, col, row)
	elif type == 'q':
		return Queen(color, col, row)
	elif type == 'ki':
		return King(color, col, row)
	