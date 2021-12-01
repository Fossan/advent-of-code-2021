import os

__location__ = os.path.realpath(os.path.join(os.getcwd(), os.path.dirname(__file__)))

data = [int(line.strip()) for line in open(f'{__location__}/input.txt', 'r')]

def solutionA():
    return data[0]

def solutionB():
    return data[1]

if __name__=="__main__":
    print(solutionA())
    print(solutionB())
