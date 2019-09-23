#  Suppose A and B are two set. A is a super set of B if all the elements in B exist in A.
#  Ex :
#    A= {1,2,3,4}
#    B={3,4}, and C= {2, 3, 5}
#  So, A ⊃ B, A is a super set of B.
#  A is not super set of C
A = set(input().split())
n = int(input())
flag = True
for i in range(n):
    sampleSet = set(input().split())
    if A.issuperset(sampleSet) != True:
        flag = False
print(flag)

