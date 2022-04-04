# currently a work in progress

W = int(input())
N = int(input())
cars = [int(input()) for _ in range(N)]
count = set()
for i in range(len(cars) - 4):
	total = sum(cars[i:i+4])
	if total <= W:
		count.add(i)
		count.add(i + 1)
		count.add(i + 2)
		count.add(i + 3)
	else:
		break
print(len(count))
# current_weight = 0
# current_cars = []
# count = []
# for i in range(len(cars)):
# 	car = cars[i]
# 	if (car <= W) and (current_weight + car <= W):
# 		current_cars.append(i)
# 		count.append(i)
# 		current_weight += car
# 	else:
# 		if current_cars != []:
# 			del current_cars[0]
# 			