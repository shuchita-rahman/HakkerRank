if __name__ == '__main__':
    n = int(input())
    arr = list(map(int, input().split()))
    arr.sort(reverse =True)
    a = max(arr)
    for i in arr:
        if i < a:
           print(i)
           break
