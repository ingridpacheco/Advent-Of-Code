from input import input

# input = '''3,4,3,1,2'''

def main():
    numbers = input.split(',')
    day = 0

    while day < 80:
        for i,n in enumerate(numbers):
            numbers[i] = int(n)
            if int(n) == 0:
                numbers[i] = 6
                numbers.append(9)
            else:
                numbers[i] -= 1

        day += 1
        print(numbers)
    
    return len(numbers)

if __name__ == "__main__":
    print(main())