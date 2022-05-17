import sys
from turtle import st

si = sys.stdin.readline

N = int(si().rstrip()) # 100000

students = []

for _ in range(N):
    a,b = si().rstrip().split()
    students.append(tuple((a,int(b))))

students.sort(key=lambda x:x[1])

for student in students:
    print(student[0],end=' ')