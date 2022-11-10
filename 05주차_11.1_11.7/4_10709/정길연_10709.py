h, w = map(int, input().split())

# 처음에 있던 자리 0 -> c 입력한 map 똑같이 하나 만들기
# 안오는 자리 -1

sky = []
for i in range(h):
    sky.append(list(map(str, input())))

# 구름 있는 자리 : 0, 구름 없는 자리 : -1
ans_map = [[0] * w for i in range(h)]

for i in range(h):
    for j in range(w):
        if(sky[i][j] == 'c'):
            ans_map[i][j] = 0
        else : 
            ans_map[i][j] = -1

# 구름 등록
for i in range(h):
     # i줄에 구름이 한 점도 없을 때 건너뛰기
    if max(ans_map[i]) == -1:
        if(i == h-1) :
            break
        i += 1

    for j in range(w):
        if ans_map[i][j] == 0 :
            if (j == w-1): 
                pass
            elif ans_map[i][j+1] != 0 and ans_map[i][j+1] == -1 :
                ans_map[i][j+1] = 1
            elif ans_map[i][j+1] != 0 and ans_map[i][j+1] != -1 :
                ans_map[i][j+1] += 1

# 결과 print          
for i in range(h):
    for j in range(w):
        print(ans_map[i][j], end=' ')
    print()