
def result(testCase):
   for i in range(0, testCase):
       n, set_A = int(input()), set(map(int, input().split()))
       n, set_B = int(input()), set(map(int, input().split()))
       
       if set_A.issubset(set_B):
           print("True")
       else:
           print("False")
     
if __name__ == '__main__':
   result(int(input()))
