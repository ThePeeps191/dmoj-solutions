D = int(input())

seqs = [34, 111, 123, 135, 147, 159,
210, 222, 234, 246, 258,
321, 333, 345, 357,
420, 432, 444, 456,
531, 543, 555, 
630, 642, 654,
741, 753, 
840, 852,
951,
1111]

cycles = D // 720
times = cycles * 31
rem = (D%720)//60*100+ D%60
cnt = 0
for seq in seqs:
	if seq <= rem:
		cnt += 1
	else:
		break
print(times + cnt)