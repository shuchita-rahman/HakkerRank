import numpy as np

n,m = map(int, input().split())
a = np.array([input().split() for i in range(0, n)], int)
print(a.transpose())
print(a.flatten())

