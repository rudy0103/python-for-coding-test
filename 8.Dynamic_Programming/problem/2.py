# p.220 실전문제 개미전사
# 난이도 중, 풀이시간 30분, 시간 제한 1초, 메모리 제한 128 MB

n = int(input())

k = list(map(int,input().split()))

d = [0] *n


d[0] = k[0]
d[1] = max(k[0],k[1])


for i in range(2, n):
    d[i] = max(d[i -1], d[i-2]+ k[i])

print(d[n-1])



