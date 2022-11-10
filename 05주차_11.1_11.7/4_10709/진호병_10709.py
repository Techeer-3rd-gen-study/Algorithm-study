H, W = map(int, input().split()) # 3, 4

joiMap = [[-1 for col in range(W)] for row in range(H)]

for i in range(H):
    WLine =  input()
    for j in range(len(WLine)):
        if WLine[j] == 'c':
            joiMap[i][j] = 0

for cnt in range(W): # 그냥 간단하게 돌아다니면서 0~w 구름 이동 최대 수까지 검사하면서 +1 시킴
    for i in range(W): # 4
        for j in range(H): # 3
            if i+1 < W :  # 배열 최대 인덱스 안넘도록 설정 
                if joiMap[j][i] == cnt and joiMap[j][i+1] == -1 : # 현재 이동수와 비교, 구름이 없던 곳에만 이동할 수 있도록 -1 체크 
                    joiMap[j][i+1] = cnt+1

for i in joiMap: 
    for j in range(W):
        print(i[j],end=" ")
    print()