from input import input

def main():
    gamma = 0
    epsilon = 0
    zero = 0
    one = 0
    numbers = input.split('\n')
    index = len(numbers[0]) - 1

    
    while (index >= 0):
        for i, n in enumerate(numbers):
            if n[index] == '0':
                zero += 1
            else:
                one += 1

            if i == len(numbers) - 1:
                if zero > one:
                    epsilon += 2**(len(numbers[0]) - 1 - index)
                else:
                    gamma += 2**(len(numbers[0]) - 1 - index)
                
                index -= 1
                zero = 0
                one = 0

    return gamma * epsilon

if __name__ == "__main__":
    print(main())