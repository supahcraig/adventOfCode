f = open('/Users/cnelson/adventOfCode/day_2_data.txt', 'r')

instructions = []

for raw in f:
    instructions.append(raw.split())

x = 0
z = 0

for instruction in instructions:
    if instruction[0] == 'forward':
        x += int(instruction[1])

    if instruction[0] == 'down':
        z += int(instruction[1])

    if instruction[0] == 'up':
        z -= int(instruction[1])

print(x * z)
