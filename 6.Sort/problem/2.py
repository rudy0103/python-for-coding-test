# p. 180 실전문제 성적이 낮은 순서로 학생 출력하기

n = int(input())

student_dic = {}
for i in range(n):
    student,grade = input().split()
    student_dic[student] = int(grade)

array = sorted(student_dic.items(), key = lambda x : x[1])


for student in array:
    print(student[0], end =' ')

