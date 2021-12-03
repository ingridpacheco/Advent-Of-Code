from input import input

def main():
    forward = 0
    depth = 0

    instructions = input.split('\n')

    for i in instructions:
        if "forward" in i:
            forward += int(i.split('forward')[1].replace(' ',''))
        elif "down" in i:
            depth += int(i.split('down')[1].replace(' ',''))
        else:
            depth -= int(i.split('up')[1].replace(' ',''))
    
    return forward * depth

if __name__ == "__main__":
    print(main())