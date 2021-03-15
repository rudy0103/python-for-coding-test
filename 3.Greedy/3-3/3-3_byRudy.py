#숫자 카드 게임
#난이도 하, 시간 제한 1초, 메모리 제한 128 MB, 기출- 2019 국가 교육기관 코딩테스트




# 행을 고른다 -> 행중에서 가장 낮은 카드를 고른다 
# 결과적으로 각 행에서 가장 낮은 수를 뽑았을 때 가장 높은 수가 되어야함

n, m = map(int, input().split())

mat = []

for i in range(n): # n 행만큼 n번 입력 받아 mat 리스트에 추가하기
    tmp = list(map(int,input().split()))
    mat.append(tmp)

# 2차원 리스트 mat가 생성됨
# 각 행에서 가장 낮은 수를 찾고 그 중 가장 큰 것을 출력
ret = []

for i in range(n):
    lowest = min (mat[i])
    ret.append(lowest)

ret.sort()
print(ret[-1])

# 문제 풀이 10분

