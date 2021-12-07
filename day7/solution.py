import os
import statistics
from math import floor, ceil

__location__ = os.path.realpath(os.path.join(os.getcwd(), os.path.dirname(__file__)))
data = list(map(int, [line.strip().split(',') for line in open(f'{__location__}/input.txt', 'r')][0]))

fuelSum = lambda progression, round, input: sum(map(lambda crab: progression(abs(crab - round(input))), data))

def solutionA():
    median = statistics.median(data)
    noProgression = lambda p: p
    return min(fuelSum(noProgression, floor, median), fuelSum(noProgression, ceil, median))

def solutionB():
    mean = statistics.mean(data)
    fuelProgression = lambda f: f * (f + 1) // 2
    return min(fuelSum(fuelProgression, floor, mean), fuelSum(fuelProgression, ceil, mean))

if __name__ == "__main__":
    print(solutionA())
    print(solutionB())
