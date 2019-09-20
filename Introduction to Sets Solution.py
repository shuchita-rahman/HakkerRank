def average(array):
    s = set()
    for i in array:
        s.add(i)
    return sum(s) / len(s)
    
if __name__ == '__main__':
    n = int(input())
    arr = list(map(int, input().split()))
    result = average(arr)
    print(result)
