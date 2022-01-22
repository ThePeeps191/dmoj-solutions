from functools import lru_cache

sq1 = tuple([int(a) for a in input().split()])
sq2 = tuple([int(a) for a in input().split()])

def get_knight_moves(sq):
	a, b = sq[0], sq[1]
	moves = []
	if (1 <= a + 1 <= 8) and (1 <= b + 2 <= 8):
		moves.append([a + 1, b + 2])
	if (1 <= a + 1 <= 8) and (1 <= b - 2 <= 8):
		moves.append([a + 1, b - 2])
	if (1 <= a + 2 <= 8) and (1 <= b + 1 <= 8):
		moves.append([a + 2, b + 1])
	if (1 <= a + 2 <= 8) and (1 <= b - 1 <= 8):
		moves.append([a + 2, b - 1])
	if (1 <= a - 1 <= 8) and (1 <= b + 2 <= 8):
		moves.append([a - 1, b + 2])
	if (1 <= a - 1 <= 8) and (1 <= b - 2 <= 8):
		moves.append([a - 1, b - 2])
	if (1 <= a - 2 <= 8) and (1 <= b + 2 <= 8):
		moves.append([a - 2, b + 1])
	if (1 <= a - 2 <= 8) and (1 <= b + 2 <= 8):
		moves.append([a - 2, b - 1])
	return moves

def check_all(moves, sq):
	for m in moves:
		if m[0] == sq[0] and m[1] == sq[1]:
			return True
	return False

@lru_cache
def quickest(sq1, sq2):
	if sq1[0] == sq2[0] and sq1[1] == sq2[1]:
		print(0)
	else:
		m = get_knight_moves(sq1)
		if check_all(m, sq2):
			print(1)
		else:
			n = []
			for move in m:
				n += get_knight_moves(move)
			if check_all(n, sq2):
				print(2)
			else:
				m = []
				for move in n:
					m += get_knight_moves(move)
				if check_all(m, sq2):
					print(3)
				else:
					n = []
					for move in m:
						n += get_knight_moves(move)
					if check_all(n, sq2):
						print(4)
					else:
						m = []
						for move in n:
							m += get_knight_moves(move)
						if check_all(m, sq2):
							print(5)
						else:
							n = []
							for move in m:
								n += get_knight_moves(move)
							if check_all(n, sq2):
								print(6)

quickest(sq1, sq2)
