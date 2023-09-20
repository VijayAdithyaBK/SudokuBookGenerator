import numpy as np
import random

def generate_sudoku():
    n = 9
    m = np.zeros((n, n), dtype=int)

    def is_valid(x, y, num):
        for i in range(n):
            if m[x][i] == num or m[i][y] == num:
                return False
        start_x, start_y = 3 * (x // 3), 3 * (y // 3)
        for i in range(3):
            for j in range(3):
                if m[start_x + i][start_y + j] == num:
                    return False
        return True

    def solve():
        for x in range(n):
            for y in range(n):
                if m[x][y] == 0:
                    possible_numbers = list(range(1, n + 1))
                    random.shuffle(possible_numbers)
                    for num in possible_numbers:
                        if is_valid(x, y, num):
                            m[x][y] = num
                            if solve():
                                return True
                            m[x][y] = 0
                    return False
        return True

    solve()

    # Randomly remove some numbers to create an unsolved puzzle
    num_to_remove = random.randint(40, 50)
    for _ in range(num_to_remove):
        while True:
            x, y = random.randint(0, n - 1), random.randint(0, n - 1)
            if m[x][y] != 0:
                m[x][y] = 0
                break

    return m
