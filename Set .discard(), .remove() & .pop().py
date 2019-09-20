n,s = int(input()), set(map(int, input().split()))

for i in range(0, int(input())):
    command = list(input().split())
    if "pop" in command:
        s.pop()
    elif "remove" in command:
        s.discard(int(command[1]))
    elif "discard" in command:
        s.discard(int(command[1]))

print(sum(s))
