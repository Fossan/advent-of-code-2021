import os
import statistics
from math import floor, ceil

__location__ = os.path.realpath(os.path.join(os.getcwd(), os.path.dirname(__file__)))
data = list(map(int, [line.strip().split(',') for line in open(f'{__location__}/input.txt', 'r')][0]))

def solutionA():
    median = statistics.median(data)
    fuelSum = lambda round: sum(map(lambda crab: abs(crab - round(median)), data))
    return min(fuelSum(floor), fuelSum(ceil))

def solutionB():
    mean = statistics.mean(data)
    fuelProgression = lambda f: f * (f + 1) // 2
    fuelSum = lambda round: sum(map(lambda crab: fuelProgression(abs(crab - round(mean))), data))
    return min(fuelSum(floor), fuelSum(ceil))

if __name__ == "__main__":
    print(solutionA())
    print(solutionB())
