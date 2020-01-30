import numpy as np

a = list(map(int, input().split()))
nArray = np.array(a)
print(nArray.reshape(3,3))
