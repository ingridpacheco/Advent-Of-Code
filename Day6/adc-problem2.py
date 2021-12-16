from input import input

# input = '''3,4,3,1,2'''

def main():
    numbers = input.split(',')
    day = 0

    numbers.sort()
    numbers_values = {}

    for i in numbers:
        if i not in numbers_values.keys():
            numbers_values[i] = 1
        else:
            numbers_values[i] += 1

    while day < 256:
        keys = numbers_values.keys()
        keys.sort()
        new_values = 0
        for k in keys:
            key_int = int(k)
            previous_value = numbers_values[k]
            numbers_values[k] = 0
            if k == '0':
                new_values = previous_value
                if '6' not in keys:
                    numbers_values['6'] = 0
                    keys.append('6')
                if '8' not in keys:
                    numbers_values['8'] = 0
                    keys.append('8')
            else:
                if str(key_int - 1) in numbers_values.keys():
                    numbers_values[str(key_int - 1)] += previous_value
                else:
                    numbers_values[str(key_int - 1)] = previous_value

            if k == '8' or k == '6':
                numbers_values[k] = new_values

        day += 1
        
    quantity = 0

    for i in numbers_values.keys():
        quantity += numbers_values[i]

    return quantity

if __name__ == "__main__":
    print(main())