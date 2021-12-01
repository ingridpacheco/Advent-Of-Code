from input import input

def main():
    numbers = input.split('\n')
    numbers = [int(n) for n in numbers]

    sliding_windows = []

    count = 0

    for i,n in enumerate(numbers):
        if i == 0:
            sliding_windows.append([n])
        elif i == 1:
            sliding_windows[0].append(n)
            sliding_windows.append([n])
        else:
            sliding_windows[len(sliding_windows) - 1].append(n)
            sliding_windows[len(sliding_windows) - 2].append(n)
            sliding_windows.append([n])

            if len(sliding_windows) - 2 != 1:
                g1 = sum(n for n in sliding_windows[len(sliding_windows) - 4])
                g2 = sum(n for n in sliding_windows[len(sliding_windows) - 3])
                
                if g2 > g1:
                    count += 1

    return count

if __name__ == "__main__":
    print(main())