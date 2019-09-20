
row,collum = input().split()
#changing sting to int
row = int(row)
collum =int(collum)
string=".|."

#Top 
for i in range(0,int(row/2)):
    print((string*i).rjust(int(collum/2)-1,'-')+string+(string*i).ljust(int(collum/2)-1, '-'))

#middle
print("WELCOME".center(collum,'-'))
 
#bottom
for i in range(int(row/2)-1, -1, -1):
    print((string*i).rjust(int(collum/2)-1,'-')+string+(string*i).ljust(int(collum/2)-1, '-'))
  
