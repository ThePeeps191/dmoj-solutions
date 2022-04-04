# work in progress

A, B = 0, 0

deck = [input() for _ in range(52)]

a = True

i = 0
while i <= 52:
	card = deck[i]
	next_cards = []
	c_points = 0
	if card == "ace":
		if i < 48:
			for j in range(1, 5):
				i += j
			next_cards.append(deck[i])
	elif card == "king":
		if i < 49:
			for j in range(1, 4):
				i += j
			next_cards.append(deck[i])
	elif card == "queen":
		if i < 50:
			for j in range(1, 3):
				i += j
			next_cards.append(deck[i])
	elif card == "jack":
		for j in range(1, 2):
			i += j
			next_cards.append(deck[i])

	for c in next_cards:
		if c in ['ace', 'king', 'queen', 'jack']:
			break
	else:
		if a:
			A += len(next_cards)
			print(f"Player A scores {len(next_cards)} point(s)")
		else:
			B += len(next_cards)
			print(f"Player B scores {len(next_cards)} point(s)")
	a = not a
	i += 1

print(f"Player A: {A} point(s).\nPlayer B: {B} point(s).")