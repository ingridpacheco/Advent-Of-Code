from input import input

def split(numbers, oxygen_bit, index):
    oxygen = []
    co2 = []
    for n in numbers:
        if n[index] == oxygen_bit:
            oxygen.append(n)
        else:
            co2.append(n)
    
    return oxygen, co2

def filter_numbers(numbers, bit, index):
    oxygen = []
    for n in numbers:
        if n[index] == bit:
            oxygen.append(n)

    return oxygen

def main():
    result = 0
    numbers = input.split('\n')
    index = 0

    c_v = sum([int(c[index]) for c in numbers])
    if c_v >= (len(numbers) / float(2)):
        oxygen_bit = '1'
    else:
        oxygen_bit = '0'
    oxygen, co2 = split(numbers, oxygen_bit, index)
    index += 1


    while (len(oxygen) > 1):
        c_v = sum([int(c[index]) for c in oxygen])
        if c_v >= (len(oxygen) / float(2)):
            oxygen_bit = '1'
        else:
            oxygen_bit = '0'
        oxygen = filter_numbers(oxygen, oxygen_bit, index)
        index += 1
    
    index = 0

    for i in range(len(oxygen[0]) - 1, -1,-1):
        result += (2**index * int(oxygen[0][i]))
        index += 1

    index = 1

    while (len(co2) > 1):
        c_v = sum([int(c[index]) for c in co2])
        if c_v >= (len(co2) / float(2)):
            oxygen_bit = '0'
        else:
            oxygen_bit = '1'
        co2 = filter_numbers(co2, oxygen_bit, index)
        index += 1

    aux_result = 0
    index = 0

    for i in range(len(co2[0]) - 1, -1,-1):
        aux_result += (2**index * int(co2[0][i]))
        index += 1

    return result * aux_result

if __name__ == "__main__":
    print(main())