instructions = [input()]

while instructions[-1] != "99999":
    instructions.append(input())
instructions.pop()

directions = []
for instruction in instructions:
    direction = int(instruction[0]) + int(instruction[1])
    steps = instruction[2:]

    if direction % 2 == 1:
        print("left " + steps)
        directions.append("left ")
    elif direction == 0:
        print(directions[-1] + steps)
    else:
        print("right " + steps)
        directions.append("right ")
