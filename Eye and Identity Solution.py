import numpy as np

#enter row and collum
n, m = map(int, input().split())

#set space for float value in numpy array
np.set_printoptions(sign=' ')

print(np.eye(n,m,k=0))

