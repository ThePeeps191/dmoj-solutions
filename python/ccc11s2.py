N = int(input())
student = [input() for _ in range(N)]
teacher = [input() for _ in range(N)]
count = 0
for a, b in zip(student, teacher):
	if a == b:
		count += 1
print(count)