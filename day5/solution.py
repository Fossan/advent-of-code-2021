import os
from collections import Counter

__location__ = os.path.realpath(os.path.join(os.getcwd(), os.path.dirname(__file__)))
data = [line.strip().split(' -> ') for line in open(f'{__location__}/input.txt', 'r')]

def solutionA():
    return countOverlaps(False)

def solutionB():
    return countOverlaps(True)

def countOverlaps(includeDiagonals):
    points = []
    getRange = lambda c1, c2: range(c1, c2 + 1) if c1 < c2 else range(c1, c2 - 1, -1)

    for coord in data:
        (x1, y1) = map(int, coord[0].split(','))
        (x2, y2) = map(int, coord[1].split(','))
        if (x1 == x2):
            for y in range(min(y1, y2), max(y1, y2) + 1):
                points.append((x1, y))
        elif (y1 == y2):
            for x in range(min(x1, x2), max(x1, x2) + 1):
                points.append((x, y1))
        elif includeDiagonals:
            xs = getRange(x1, x2)
            ys = getRange(y1, y2)
            for x, y in zip(xs, ys):
                points.append((x, y))

    return sum(v > 1 for v in Counter(points).values())

if __name__ == "__main__":
    print(solutionA())
    print(solutionB())
