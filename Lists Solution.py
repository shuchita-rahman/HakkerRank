if __name__ == '__main__':
    n = int(input())
    l = []
    for i in range(0, n):

        s = input().split(" ")
        command = s[0]

        if command == 'insert':
            l.insert(int(s[1]), int(s[2]))
        elif command == 'print':
            print(l)
        elif command == 'remove':
            l.remove(int(s[1]))
        elif command == 'sort':
            l.sort()
        elif command == 'append':
            l.append(int(s[1]))
        elif command == 'pop':
            l.pop()
        elif command == 'reverse':
            l.reverse()


