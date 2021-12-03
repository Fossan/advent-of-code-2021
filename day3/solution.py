import os
import operator

__location__ = os.path.realpath(os.path.join(os.getcwd(), os.path.dirname(__file__)))

data = [(line.strip()) for line in open(f'{__location__}/input.txt', 'r')]

findBits = lambda bits, idx, val: [b for b in bits if b[idx] == val]

def solutionA():
    binary = ''
    for i in range(len(data[0])):
        zeros = findBits(data, i, '0')
        ones = findBits(data, i, '1')
        binary += ('0' if len(zeros) > len(ones) else '1')
        
    gamma = int(binary, 2)
    epsilon = gamma ^ 0xfff
    
    return gamma * epsilon
        
def solutionB():
    oxygen = findCommon(data, operator.gt)
    co2 = findCommon(data, operator.le)

    return int(oxygen, 2) * int(co2, 2)

def findCommon(numbers, operator, index = 0):
    if (len(numbers) == 1): return numbers[0]

    zeros = findBits(numbers, index, '0')
    ones = findBits(numbers, index, '1')

    return findCommon(zeros if operator(len(zeros), len(ones)) else ones, operator, index + 1)

if __name__ == "__main__":
    print(solutionA())
    print(solutionB())
