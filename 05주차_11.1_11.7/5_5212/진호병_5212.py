import copy

def checkSum(x,y):
    ox = [0,0,-1,1]
    oy = [-1,1,0,0]
    cnt = 0
    for i in range(4) : 
        X = x + ox[i] 
        Y = y + oy[i]

        if (0<=X<R) and (0<=Y<C) :
            if dadoMap[X][Y] == "X" :
                continue
            else : 
                cnt += 1
        else :  # 배열 범위 외의 것들은 모두 바다임 
            cnt += 1

    if (cnt>=3):
        copyMap[x][y] = "."



R, C = map(int, input().split())

dadoMap = []
# 후에 섬 존재하는 땅의 최소 크기 구하기 위한 x,y값
xArr = []
yArr = []

for i in range(R):
    dadoMap.append(list(input()))

copyMap = copy.deepcopy(dadoMap) # 이래야 아예 새로운 배열을 할당 받음 그냥 복사하면 얕은 복사됨


for i in range(R): # 5
    for j in range(C): # 3
        if dadoMap[i][j] == 'X': # X 일때 함수로 넘겨서 돌리자 
            # 함수 돌려서 인접 땅에 바다 몇개 있나 검사
            checkSum(i,j)

for i in range(R): # 5
    for j in range(C): # 3
        if copyMap[i][j] == "X": # 50년 후의 땅의 X의 x,y값 검사
            xArr.append(i)
            yArr.append(j) 

for i in range(min(xArr), max(xArr)+1): #1~2
    for j in range(min(yArr), max(yArr)+1): # 1~7
        print(copyMap[i][j], end="")
    print()
