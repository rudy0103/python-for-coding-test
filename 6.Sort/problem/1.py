# p.178 실전문제 위에서 아래로

n = int(input())

num_list=[]
for i in range(n):
    num_list.append(int(input()))

num_list.sort(reverse=True)

for i in num_list:
    print(i, end=' ')