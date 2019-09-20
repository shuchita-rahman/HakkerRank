#take input
n, set1 = int(input()),set(input().split())
m,set2 = int(input()),set(input().split())

#put differnce value of set2 in subSetOne
subSetOne = set1.difference(set2)

#put differnce value of set1 in subSetTwo
subSetTwo =set2.difference(set1)

#concante two set
result = subSetOne.union(subSetTwo)

#sort the result and print it
print("\n".join(sorted(result,key= int)))
