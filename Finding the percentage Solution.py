if __name__ == '__main__':
    n = int(input())
    student_marks = {}
    for _ in range(n):
        name, *line = input().split()
        student_marks[name] = format((sum(list(map(float, line)))/3), '.2f')
    query_name = input()
    print(student_marks[query_name])
