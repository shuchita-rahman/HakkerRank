def birthdayCakeCandles(ar):
    ar.sort(reverse= True)
    candale = 0
    num = max(ar)

    for i in ar:
        if i == num:
            candale= candale+ 1
        else:
            break
    return candale

if __name__ == '__main__':
    ar_count = int(input())
    ar = list(map(int, input().rstrip().split()))
    print(ar)
    
