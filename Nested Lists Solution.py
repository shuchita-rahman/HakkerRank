if __name__ == '__main__':

    studentInfo =[]

    for i in range(0, int(input())):
        studentInfo.append([input(), float(input())])
    
    studentInfo.sort(key=lambda x:x[1])
    minScore = studentInfo[0][1]
    secondLowest = []
    secMin = float('inf')
    flag = 0 

    for i in range(1, len(studentInfo)):
        if (minScore != studentInfo[i][1] and flag == 0) or secMin == studentInfo[i][1]:
            secondLowest.append(studentInfo[i][0])
            flag =1
            secMin = studentInfo[i][1]
    
    secondLowest.sort()
    for i in secondLowest:
        print(i)


