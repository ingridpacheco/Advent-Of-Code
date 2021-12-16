from input import input

def increase_value(matriz, y, x, arrays, quantity):
    if matriz[x] is None:
        matriz[x] = [0] * 1000
    matriz[x][y] += 1
    if (matriz[x][y] >= 2 and (x,y) not in arrays):
        quantity += 1
        arrays.append((x,y))

    return matriz, arrays, quantity

def main():
    numbers = input.split('\n')
    matriz = [None] * 1000
    quantity = 0
    arrays = []

    for n in numbers:
        print(n)
        b, e = n.split(' -> ')
        x1,y1 = b.split(',')
        x2,y2 = e.split(',')

        if (int(x1) == int(x2)):
            if (int(y1) > int(y2)):
                for i in range(int(y1), int(y2) - 1, -1):
                    matriz, arrays, quantity = increase_value(matriz, i, int(x1), arrays, quantity)

            if (int(y2) > int(y1)):
                for i in range(int(y1), int(y2) + 1):
                    matriz, arrays, quantity = increase_value(matriz, i, int(x1), arrays, quantity)
        elif (int(y1) == int(y2)):
            if (int(x1) > int(x2)):
                for i in range(int(x1), int(x2) - 1, -1):
                    matriz, arrays, quantity = increase_value(matriz, int(y1), i, arrays, quantity)

            if (int(x2) > int(x1)):
                for i in range(int(x1), int(x2) + 1):
                    matriz, arrays, quantity = increase_value(matriz, int(y1), i, arrays, quantity)
        else:
            if (int(x1) > int(x2) and int(y1) < int(y2)):
                x = int(x1)
                y = int(y1)
                while (x >= int(x2)):
                    matriz, arrays, quantity = increase_value(matriz, y, x, arrays, quantity)
                    x -= 1
                    y += 1

            if (int(x1) > int(x2) and int(y1) > int(y2)):
                x = int(x1)
                y = int(y1)
                while (x >= int(x2)):
                    matriz, arrays, quantity = increase_value(matriz, y, x, arrays, quantity)
                    x -= 1
                    y -= 1

            if (int(x1) < int(x2) and int(y1) < int(y2)):
                x = int(x1)
                y = int(y1)
                while (x <= int(x2)):
                    matriz, arrays, quantity = increase_value(matriz, y, x, arrays, quantity)
                    x += 1
                    y += 1

            if (int(x1) < int(x2) and int(y1) > int(y2)):
                x = int(x1)
                y = int(y1)
                while (x <= int(x2)):
                    matriz, arrays, quantity = increase_value(matriz, y, x, arrays, quantity)
                    x += 1
                    y -= 1

    return quantity

if __name__ == "__main__":
    print(main())