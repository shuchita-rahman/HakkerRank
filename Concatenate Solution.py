import numpy as np

n, m, p = map(int, input().split())
arrayOne = np.array([input().split() for _ in range(n)], int)
arrayTwo = np.array([input().split() for _ in range(m)], int)

print(np.concatenate([arrayOne, arrayTwo], axis = 0))

