n, set1 = int(input()), set(map(int, input().split()))
n, set2 = int(input()), set(map(int, input().split()))

result = set1.symmetric_difference(set2)
print(len(result))
