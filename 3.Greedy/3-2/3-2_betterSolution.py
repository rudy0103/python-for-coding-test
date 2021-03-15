# 난이도 하, 풀이 시간 30분, 시간 제한 1초, 메모리 제한 128MB


# 수열이 반복되어 더해지는 문제임으로 좀 더 효율적인 문제풀이를 할 수 있다.


N,M,K = map(int,input().split())
#N = 배열크기,  M= 숫자가 더해지는 횟수, K=연속해서 K번을 초과하여 더할 수 없다.


arr = list(map(int, input().split()))


# K번 초과하여 연속해서 더하지만 않으면 됨
# 가장 큰수와 두번째 큰수만 사용됨 -> max1, max2 찾기
# max1과 max2가 반복되는 규칙 -> max1은 k번 max2는 한번 즉 M번보다 작은수 한해서 k+1이 반복됨


max1 = max(arr)
arr.remove(max1)
max2 = max(arr)

count = M//(K+1) # 수열이 반복되는 횟수

sumOfRepeat = max1*K + max2

result = sumOfRepeat * count + max1 *(M%(K+1))
# 반복되는 횟수만큼 더하고 M을 K+1로 
#모듈러 연산한 만큼 max1이랑 곱해서 더함

print(result)


# # -------------------교재 답안 p.95---------------

# n, m ,k = map(int, input().split())
# data = list(map(int, input().split()))

# data.sort()
# first = data[n-1] # 가장 큰 수
# second = data[n-2] # 두 번째로 큰 수


# # 가장 큰 수가 더해지는 횟수 계산
# count = int(m/(k+1)) * k 
# count += m % (k + 1)

# result = 0
# result += (count) * first # 가장 큰 수 더하기
# result += (m - count) * second # 두 번째로 큰 수 더하기

# print(result)


