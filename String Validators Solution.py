if __name__ == '__main__':
    s = input()
    flag = [False]* 5
    for a in s:

        if a.isalnum():
            if flag[0]!= True:
                flag[0] = True;
        if a.isalpha():
            if flag[1] != True:
               flag[1] = True;
        if a.isdigit():
            if flag[2] != True:
               flag[2] = True;
        if a.islower()== True:
            if flag[3] != True:
               flag[3] = True;
        if a.isupper():
            if flag[4] != True:
               flag[4] = True;  
    for i in flag:
        print(i) 


