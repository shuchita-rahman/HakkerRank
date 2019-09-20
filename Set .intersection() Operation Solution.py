n, set1 = int(input()), set(map(int, input().split()))
n, set2 = int(input()), set(map(int, input().split()))

result = set1.intersection(set2)
print(len(result))
