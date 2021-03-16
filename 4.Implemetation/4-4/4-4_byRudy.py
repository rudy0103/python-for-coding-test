# 실전문제 게임개발
# 난이도 중, 풀이 시간 40분, 시간제한 1초, 메모리 제한 128MB

n,m = map(int, input().split()) # n,m을 입력받는다 N은 세로크기, M은 가로크기

a , b, d = map(int,input().split()) # 캐릭터가 위치한 좌표(A,B)와 방향 d
                                    # 방향 d는 (0,1,2,3) 북 동 남 서

# 방향에 따라 움직이는 타입이 형성

# 90도 회전 서 ->남 ->동 >북->서
#           3 -> 2 ->1 -> 0 ->3

def changeDirection(dd):
    if dd == 0:
        dd = 3
    else:
        dd -= 1

    return dd




move_type=[(-1,0),(0,1),(1,0),(0,-1)] # 북, 동, 남, 서 0, 1, 2, 3 



Map = []

for i in range(m):
    Map.append(list(map(int, input().split())))

Map[a][b]=2 # 처음 위치는 방문한 곳으로 표시
visited = 1 # 방문한곳은 1부터 시작


while True:
    turn = 0
    for i in range(4): # 4가지 방향에 대해서 이동할 수 있는 곳인지 확인
        d = changeDirection(d)
        da,db = move_type[d]

        if Map[a+da][b+db] == 0: #이동할 수 있는 곳이면 이동하고 방문 표시함 
            a,b = a+da, b+ db #이동
            Map[a][b] = 2 # 방문표시
            # print(Map)
            move+=1
            break
        else:
            turn +=1 # 방문할 수 없는곳이면 turn을 증가시킴으로써 4방향 모두 검사한 후 turn은 4가 된다.


    if turn == 4: # 네 방향 모두 검사하고 뒤로 갈 수 있는지 검사 . 바다이면 끝내고 바다가 아니면 뒤로감
        da,db = move_type[d]
        if Map[a-da][b-db]==1:
            break
        else:
            a,b = a-da,b-db

print (move)


#문제 풀이 50분

# 평면 좌표의 x,y와 매트릭스 행열이 헷갈림
# 체계적으로 접근하는게 서툴러서 시간이 오래걸림
# 디버깅이 부족함
