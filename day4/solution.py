import os
import numpy as np

__location__ = os.path.realpath(os.path.join(os.getcwd(), os.path.dirname(__file__)))

def getNumbersAndBoards():
    bingoNumbers, *boards = open(f'{__location__}/input.txt')
    boards = np.loadtxt(boards, int).reshape(-1, 5, 5)
    return [bingoNumbers, boards]

def solutionA():
    bingoNumbers, boards = getNumbersAndBoards()
    for number in [int(n) for n in bingoNumbers.split(',')]:
        markedBoards = markBoards(boards, number)
        winningBoard = findWinningBoard(markedBoards)
        if winningBoard.any():
            return (boards * ~markedBoards)[winningBoard].sum() * number
        
def solutionB():
    bingoNumbers, boards = getNumbersAndBoards()
    for number in [int(n) for n in bingoNumbers.split(',')]:
        markedBoards = markBoards(boards, number)
        winningBoard = findWinningBoard(markedBoards)
        if len(boards) > 1 & winningBoard.any():
            boards = boards[~winningBoard]
        else:
            return (boards * ~markedBoards)[winningBoard].sum() * number

def markBoards(boards, number):
    boards[boards == number] = False
    markedBoards = boards == False
    return markedBoards

def findWinningBoard(markedBoards):
    return (markedBoards.all(1) | markedBoards.all(2)).any(1)

if __name__ == "__main__":
    print(solutionA())
    print(solutionB())
