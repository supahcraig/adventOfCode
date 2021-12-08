f = open('/Users/cnelson/adventOfCode/day_1_data.txt', 'r')

data = []
revised_data = []
for d in f:
    data.append(int(d))

increase = 0
decrease = 0

# transform measurement set into triples
for i, measurement in enumerate(data):
    try:
        new_measurement = data[i] + data[i+1] + data[i+2]

        revised_data.append(new_measurement)
    except:
        pass

current_measurement = revised_data[0]

for measurement in revised_data:
    if measurement > current_measurement:
        increase += 1
    if measurement < current_measurement:
        decrease += 1

    current_measurement = measurement

print(f'there were {increase} increases, and {decrease} decreases.')
