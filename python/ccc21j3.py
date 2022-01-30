instructions = [input()]

while instructions[-1] != "99999":
    instructions.append(input())
instructions.pop()

for instruction in instructions:
    direction = int(instruction[0]) + int(instruction[1])
    steps = instruction[2:]

    if direction % 2 == 1:
        print("left " + steps)
        last_direction = "left "
    elif direction == 0:
        print(last_direction + steps)
    else:
        print("right " + steps)
        last_direction = "right "
