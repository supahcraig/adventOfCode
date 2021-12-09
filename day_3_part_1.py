f = open('/Users/cnelson/adventOfCode/day_3_data.txt', 'r')

codes = []

for raw in f:
    codes.append(raw)

#codes = ['011011010001', '011011010001', '011011010001']
#print(codes)


def identify_bit(codes, bit, max=True):
    bit1 = 0
    bit0 = 0

    for code in codes:
        if code[bit] == '1':
            bit1 += 1
        else:
            bit0 += 1

    if max:
        if bit1 > bit0:
            return 1
        else:å
            return 0
    else:
        if bit1 < bit0:
            return 1
        else:
            return 0


gamma = [identify_bit(codes, 0),
         identify_bit(codes, 1),
         identify_bit(codes, 2),
         identify_bit(codes, 3),
         identify_bit(codes, 4),
         identify_bit(codes, 5),
         identify_bit(codes, 6),
         identify_bit(codes, 7),
         identify_bit(codes, 8),
         identify_bit(codes, 9),
         identify_bit(codes, 10),
         identify_bit(codes, 11)
         ]

epsilon = [identify_bit(codes, 0, False),
         identify_bit(codes, 1, False),
         identify_bit(codes, 2, False),
         identify_bit(codes, 3, False),
         identify_bit(codes, 4, False),
         identify_bit(codes, 5, False),
         identify_bit(codes, 6, False),
         identify_bit(codes, 7, False),
         identify_bit(codes, 8, False),
         identify_bit(codes, 9, False),
         identify_bit(codes, 10, False),
         identify_bit(codes, 11, False)
         ]

print(gamma)
print(epsilon)

def decimal_convert(q):
    decimal = 0
    for i, bit in enumerate(reversed(q)):
        decimal += bit * pow(2, i)

    return decimal

print(decimal_convert(gamma))
print(decimal_convert(epsilon))

print(decimal_convert(gamma) * decimal_convert(epsilon))
