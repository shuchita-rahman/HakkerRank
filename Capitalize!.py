def solve(s):
    flag = 0
    result = ""

    for i in s:
        if flag == 0:
            result= result + i.upper()
            flag = 1
        elif i == ' ' :
            result= result + i
            flag = 2
        elif flag == 2:
             result= result + i.upper()
             flag = 3
        else:
            result= result + i
    return result
    
