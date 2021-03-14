# Number spiral diagonals

import numpy as np

size = (1001, 1001)
zeros = np.zeros(size, dtype=int)


class Spiral:
    def __init__(self, array):
        self.array = array
        self.size = len(array[0])
        self.currentX = self.size // 2
        self.currentY = self.size // 2
        self.currentN = 1
        self.sum = self.getsum()

    def next_n(self):
        if self.currentN == 1:
            self.array[self.currentX][self.currentY] = 1

        try:
            above = self.array[self.currentX - 1][self.currentY]
        except BaseException:
            above = 0
        try:
            right = self.array[self.currentX][self.currentY + 1]
        except BaseException:
            right = 0
        try:
            left = self.array[self.currentX][self.currentY - 1]
        except BaseException:
            left = 0
        try:
            below = self.array[self.currentX + 1][self.currentY]
        except BaseException:
            below = 0

        self.currentN += 1

        if (below > 0 and right == 0) or self.currentN == 2:
            self.currentY += 1
        elif left > 0 and below == 0 and self.currentY != 0:
            self.currentX += 1
        elif above > 0 and left == 0:
            self.currentY -= 1
        elif right > 0 and above == 0:
            self.currentX -= 1

        self.array[self.currentX][self.currentY] = self.currentN


    def fill_spiral(self):
        while (self.currentN < (self.size**2)):
            self.next_n()


    def getsum(self):
        self.fill_spiral()
        count = -1
        for i in range(self.size):
            count += self.array[i][i]
            count += self.array[i][self.size - i - 1]
        return count


array = Spiral(zeros)
array.sum
