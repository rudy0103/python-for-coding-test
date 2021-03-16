# 예제 4-2 시각
# 난이도 하, 풀이 시간 15분, 시간 제한 2초, 메모리 제한 128MB

n = int(input())



count = 0
#N:00:00 ~ N:59:59 까지 시간을 무시하고 1시간 동안세어야 하는 경우의 수

m,s =0,0


for i in range(3600):
    if s < 59:
        s+=1
    else:
        s=0
        m+=1
    
    if '3' in str(s) or '3' in str(m):
        count+=1

# print(count)


# count = 1575임
special_case=3600# N이 3 이거나 13이거나 23일때는 분과 초에 관계없이 3600개

ret=0
for i in range(n+1):
    if i in [3, 13, 23]:
        ret+=3600
    else:
        ret+=count

print(ret)

# #답안 예시---------------------------------------------

# h = int(input())

# count = 0

# for i in range(n+1):
#     for j in range(60):
#         for k in range(60):
#             #매 시각 안에 '3'이 포함되어 있다면 카운트 증가
#             if '3' in str(i) + str(j) +str(k):
#                 count += 1

# print(count)