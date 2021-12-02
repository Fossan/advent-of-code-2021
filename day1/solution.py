import os

__location__ = os.path.realpath(os.path.join(os.getcwd(), os.path.dirname(__file__)))

data = [int(line.strip()) for line in open(f'{__location__}/input.txt', 'r')]

def solutionA():
    return countIncreases(data)

def solutionB():
    return countIncreases([sum(data[i : i + 3]) for i in range(0, len(data) - 2)])

def countIncreases(list):
    count = 0
    for index, element in enumerate(list):
        if element > list[index - 1]:
            count += 1
    return count

if __name__ == "__main__":
    print(solutionA())
    print(solutionB())