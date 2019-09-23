
setSize, givenSet = int(input()), set(map(int,input().split()))
testCase = int(input())

for i in range(testCase):
    querySet = list(input().split())
    
    if "intersection_update" in querySet:
          givenSet.intersection_update(set(map(int,input().split())))
    elif "update" in querySet:
          givenSet.update(set(map(int,input().split())))
    elif "symmetric_difference_update" in querySet:
          givenSet.symmetric_difference_update(set(map(int,input().split())))  
    else:   
          givenSet.difference_update(set(map(int,input().split())))

print(sum(givenSet))

