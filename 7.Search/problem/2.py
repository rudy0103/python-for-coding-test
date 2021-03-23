# p.201 실전문제 떡복이 떡 만들기
# 난이도 중, 풀이 시간 40분 , 시간 제한 2초, 메모리 제한 128MB

n, m = map(int, input().split())

x = list(map(int, input().split()))




x.sort()

start = 0
end = x[-1]

result = 0

h = 0

while start<=end:
    sum = 0
    mid = (start+end) //2

    for i in x:
        if i - mid > 0:
            sum = sum + (i - mid)

    if sum == m:
        h=mid
        break
    elif sum < m:
        end = mid - 1
    else:
        h = mid # 최대한 덜 잘랐을 때가 정답이므로, 여기에서 h에 기록 ***
        start = mid + 1
        
    

    
     

print(h)


# 문제의 시간제한 조건을 해결하기위해선 h = h-1 이되면 안됨
# 즉 최적의 h를 찾기 위해서 이진탐색같은 알고리즘을 넣어야함
