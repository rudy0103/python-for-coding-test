# p.217 실전 문제 1로 만들기
# 난이도 중하, 풀이 시간 20분, 시간 제한 1초, 메모리 제한 128MB

x = int(input())

count = 0

while x != 1:

    if x % 5 == 0:
        x //= 5
        count+=1
    elif x % 4 == 0:
        x //= 5
        count += 1

    elif x % 3 == 0:
        x //= 3
        count+=1
    else:
        x -=1
        count +=1

print(count)

