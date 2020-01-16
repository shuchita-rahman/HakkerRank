#take Input                                     #Suppose
n, m = input().split()                          # n = 3, m = 2
arrN = input().split()                          #arrN =[1, 3 , 5]
a = set(input().split())                        # a = {"1", "2"}
b = set(input().split())                        # b = {"5", "7"} 

#List Compreshion 
print(sum([(i in a) - (i in b)for i in arrN]))  # True = 1, False = 0; S0 sum(1,0,-1)


                                                  

