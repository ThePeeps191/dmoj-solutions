vals = input().split()
offset = int(vals[0]) - 1
days = int(vals[1])
print("Sun Mon Tue Wed Thr Fri Sat")
print("    " * offset, end = "")
begin = True
for day in range(1, days + 1):
	if begin:
		begin = False
	else:
		print(" ", end = "")
	print(f"{day : 3}", end = "")
	if (day + offset) % 7 == 0:
		print()
		begin = True  
if (days + offset) % 7 != 0:
	print()