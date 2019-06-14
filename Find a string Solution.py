def count_substring(string, sub_string):
    
    subLength = len(sub_string) - 1
    strLength = len(string) - subLength
    count = 0
    for i in range(0,strLength):
       
        if string[i:i+subLength+1] == sub_string:
           count = count + 1

    return count

if __name__ == '__main__':
    string = input().strip()
    sub_string = input().strip()
    
    count = count_substring(string, sub_string)
    print(count)
