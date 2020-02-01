import numpy

row, col = map(int, input().split())
a = numpy.array([input().split() for _ in range(row)], int) 
b = numpy.array([input().split() for _ in range(row)], int)

print(numpy.add(a, b))
print(numpy.subtract(a, b))
print(numpy.multiply(a, b))
print(numpy.array(a/b, int))
print(numpy.mod(a, b))
print(numpy.power(a, b))
