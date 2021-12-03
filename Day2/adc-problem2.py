from input import input

def main():
    forward = 0
    depth = 0
    aim = 0

    instructions = input.split('\n')

    for i in instructions:
        if "forward" in i:
            forward_value = int(i.split('forward')[1].replace(' ',''))
            forward += forward_value
            depth += (forward_value * aim)
        elif "down" in i:
            aim += int(i.split('down')[1].replace(' ',''))
        else:
            aim -= int(i.split('up')[1].replace(' ',''))
    
    return forward * depth

if __name__ == "__main__":
    print(main())