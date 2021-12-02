import os

__location__ = os.path.realpath(os.path.join(os.getcwd(), os.path.dirname(__file__)))

data = [(line.strip()) for line in open(f'{__location__}/input.txt', 'r')]
instructions = [instruction.split() for instruction in data]

def solutionA():
    calculate = lambda command: sum([int(i[1]) for i in instructions if i[0] == command])

    depth = calculate('down') - calculate('up')
    horizontal = calculate('forward')

    return horizontal * depth

def solutionB():
    depth, horizontal, aim = 0, 0, 0

    for instruction in instructions:
        match(instruction):
            case 'down', value: aim += int(value)
            case 'up', value: aim -= int(value)
            case 'forward', value: horizontal += int(value); depth += aim * int(value)
            
    return horizontal * depth

if __name__ == "__main__":
    print(solutionA())
    print(solutionB())
