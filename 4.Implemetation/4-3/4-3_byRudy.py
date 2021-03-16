#실전 문제 왕실의 나이트 p.115

state = input()

x = ord(state[0]) # a~h 97~104
y = int(state[1])



# a = 97, h = 104

#RLUD 에 따른 이동

dx = [1,-1,0,0]
dy = [0, 0, -1 ,1]

move_types=['R','L','U','D']

posible_case = ['RRU','RRD','LLU','LLD','UUR','UUL','DDR','DDL']

ret = 0

for case in posible_case:
    nx= x
    ny= y
    for move in case:
        for i in range(len(move_types)):
            if move == move_types[i]:
                nx+= dx[i]
                ny+= dy[i]

    if nx <97 or ny <1 or nx > 104 or ny >9:
        continue

    ret+=1


print(ret)
        




