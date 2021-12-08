f = open('/Users/cnelson/adventOfCode/day_2_data.txt', 'r')

instructions = []

for raw in f:
    instructions.append(raw.split())

x = 0
z = 0
aim = 0

for instruction in instructions:
    if instruction[0] == 'forward':
        x += int(instruction[1])
        z += ( int(instruction[1]) * aim )

    if instruction[0] == 'down':
        aim += int(instruction[1])

    if instruction[0] == 'up':
        aim -= int(instruction[1])

print(x * z)
