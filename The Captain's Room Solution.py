#take input
k = int(input())
l = list(map(int, input().split()))
inputSet = set()

#travarse set
for i in l:
# check it "i" is in set "inputSet"
   if i not in inputSet:
       captainRoom = i
    inputSet.add(i)

print(captainRoom)   

