# p.197  실전문제 부품 찾기
# 난이도 중하, 풀이 시간 30분, 시간 제한 1초, 메모리 제한 128MB

n = int(input())

item_list = list(map(int, input().split()))

m = int(input())

request_item_list = list(map(int, input().split()))

for i in request_item_list:
    if i in item_list:
        print('yes', end=' ')
    else:
        print('no', end =' ')