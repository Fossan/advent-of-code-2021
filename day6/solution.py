import os
from collections import Counter

__location__ = os.path.realpath(os.path.join(os.getcwd(), os.path.dirname(__file__)))
data = list(map(int, [line.strip().split(',') for line in open(f'{__location__}/input.txt', 'r')][0]))

def solutionA():
    return countFishes(80)

def solutionB():
    return countFishes(256)

def countFishes(days):
    fishes = Counter(data)
    for _ in range(days):
        newFishes = fishes[0]
        for i in range(8):
            fishes[i] = fishes[i+1]
        fishes[6] += newFishes
        fishes[8] = newFishes
    return sum(fishes.values())

if __name__ == "__main__":
    print(solutionA())
    print(solutionB())
