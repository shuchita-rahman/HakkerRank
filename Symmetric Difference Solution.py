#take input
n, set1 = int(input()),set(input().split())
m,set2 = int(input()),set(input().split())

#put values of set2 in subSetOne which are not in set1
subSetOne = set1.difference(set2)

#put  value of set1 in subSetTwo which are not in set2
subSetTwo =set2.difference(set1)

#concante two set
result = subSetOne.union(subSetTwo)

#sort the result and print it
print("\n".join(sorted(result,key= int)))


