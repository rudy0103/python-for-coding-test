# 난이도 하, 시간 제한 1초 , 메모리 제한 128MB, 기출: 2018 E 기업 알고리즘 대회

# n ,k = map(int,input().split())


# count = 0

# while n !=1:
#     if n % k ==0:
#         n /= k
#         count+=1

#     else:
#         n-=1
#         count+=1


# print(count)



#문제 풀이 5분

n ,k = map(int,input().split())


count = 0


while n !=1: # n이 1이 아닐경우 반복
    if n % k ==0: # n을 k로 나누었을 때 나머지가 0이라면 즉 n이 k 의 배수라면
        n /= k # n을 k로 나누고 
        count+=1 # count를 1추가

    else: # n을 k로 나누었을 때 나머지가 0이 아닐경우 
        if n > k: # n이 k보다 클 때
            n-= (n%k) # n에서 n%k를 빼줌으로서 n을 k의 배수로 만든다.
            count+=1
        else:
            # n이 k보다 작으면 n-1만큼 count에 더한다.
            count+=(n-1)
            break


print(int(count))
