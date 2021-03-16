# 예제 4-1 상하좌우 p110

n = int(input())

move = list(map(str,input().split()))

location = [1,1]

for i in move:
    if i == 'L' :
        if location[1] != 1:
            location[1]=location[1]-1
    if i == 'R' :
        if location[1] != n:
            location[1] = location[1]+1
    if i == 'U':
        if location[0] != 1:
            location[0] = location[0]-1

    if i == 'D':
        if location[0] != n:
            location[0] = location[0]+1

print(location[0],location[1])


#----- 모범 답안

n = int(input())

x,y =1,1
plans = input().split()

# L,R,U,D 에 따른 이동 방향
dx = [0,0,-1,1]
dy = [-1,1,0,0]
move_types = ['L','R','U','D']


for plan in plans:
    #이동 후 좌표 구하기
    for i in range(len(move_types)):
        if plan == move_types[i]:
            nx = x + dx[i]
            ny = y + dy[i]

    # 공간을 벗어나는 경우 무시

    if nx < 1 or ny < 1 or nx > n or ny >n:
        continue

    # 이동 수행
    x,y = nx, ny


print(x, y)

            