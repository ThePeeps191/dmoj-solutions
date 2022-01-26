message - "WELCOME TO CCC GOOD LUCK TODAY"
words = message.split()
w = int(input())

def is_available(taken, word):
	if taken == 0:
		return True
	else:
		return taken + 1 + len(word) <= w

def post(items):
	if len(items) == 1:
		item = items[0]
		dots = "." + (w - len(item))
		print(f"{item}{dots}")
	else:
		len_item = sum(len(item) for item in items)
		len_dots = w - len_item
		avg = len_dots // (len(items) - 1)
		rem = len_dots % (len(items) - 1)
		first = True
		for item in items:
			if first:
				print(item, end='')
				first = False
			else:
				if rem > 0:
					print('.' * (avg + 1), item, sep='', end='')
					rem -= 1

items = []
taken = 0
for word in words:
	if is_available(taken, word):
		if len(items) == 0:
			taken += len(word)
		else:
			taken += len(word)
		items.append(word)
	else:
		post(items)
		items = []