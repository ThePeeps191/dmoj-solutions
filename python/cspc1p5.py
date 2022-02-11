N = int(input())

scores = {}

for _ in range(N):
	sub, score = input().split()
	scores[sub] = score.split("%")[0]

drop = input()

print(f"{round(sum([scores[key] for key in scores]) / len(scores), 2)}%")

dropped = scores.copy()
del dropped[drop]

print(f"{round(sum([dropped[key] for key in dropped]) / len(dropped), 2)}%")

should_drop = min(scores.values())

for key in scores:
	if scores[key] == should_drop:
		drop_it = scores[key]

print(drop_it)

best_dropped = scores.copy()
del best_dropped[drop_it]
print(f"{round(sum([best_dropped[key] for key in best_dropped]) / len(best_dropped), 2)}%")
print(f"You are {95 - round(sum([best_dropped[key] for key in best_dropped]) / len(best_dropped), 2)}% away from your goal.")