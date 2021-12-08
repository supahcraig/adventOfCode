f = open('/Users/cnelson/adventOfCode/day_1_data.txt', 'r')

data = []

for d in f:
    data.append(int(d))

current_measurement = data[0]
increase = 0
decrease = 0

for measurement in data:
    if measurement > current_measurement:
        increase += 1
    if measurement < current_measurement:
        decrease += 1

    current_measurement = measurement

print(f'there were {increase} increases, and {decrease} decreases.')
