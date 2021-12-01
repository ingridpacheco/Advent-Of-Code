from input import input

def main():
    numbers = input.split('\n')
    numbers = [int(n) for n in numbers]

    count = 0

    for i,n in enumerate(numbers):
        if (i != 0 and n > numbers[i - 1]):
            count += 1
    
    return count

if __name__ == "__main__":
    print(main())