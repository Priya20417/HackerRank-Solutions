if __name__ == '__main__':
    n = int(input())
    student_marks = {}
    for _ in range(n):
        name, *line = input().split()
        scores = list(map(float, line))
        student_marks[name] = scores
    query_name = input()
    k=student_marks.get(query_name)
    sums=0
    for i in (k):
        sums += i
    avg=sums/float(len(k))
    print(format(avg, '.2f'))

            
