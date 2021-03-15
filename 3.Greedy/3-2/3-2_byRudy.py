# 난이도 하, 풀이 시간 30분, 시간 제한 1초, 메모리 제한 128MB

N,M,K = map(int,input().split())
#N = 배열크기,  M= 숫자가 더해지는 횟수, K=연속해서 K번을 초과하여 더할 수 없다.


arr = list(map(int, input().split()))


# N,M,K = 5,7,2

# arr = [3,4,3,4,3]

# K번 초과하여 연속해서 더하지만 않으면 됨
# 가장 큰수와 두번째 큰수만 사용됨 -> max1, max2 찾기

max1 = max(arr)
arr.remove(max1)
max2 = max(arr)

count = 0
sum = 0

while count<M:
    for i in range(K):
        count+=1
        sum+=max1
        if count == M:
            break
    if count < M:
        count+=1
        sum+=max2



print(sum)


#문제풀이 15분

