# 백준 10709번 : 기상캐스터
# 처음 구름이 있던 자리 = 0 , 구름 안 뜰 예정 = -1 
# 문제 풀때 sky리스트에서 -1,0,1로 숫자를 변경하려했는데, 잘 되지 않아서, 따로 answer리스트를 만들어주었다. 

h, w = map(int, input().split())
sky = [input() for _ in range(h)]

for i in range(h):
    time = 1     # 구름 오는 시간    
    cloud = False 
    answer = [[0] * w for _ in range(h)]

    for j in range(w):

        if sky[i][j] == 'c':   # 구름 있던 자리 
            cloud = True
            answer[i][j] = 0
            time = 1  

        elif not cloud and sky[i][j] == '.':   # 전에 구름이 나오지 않은 경우 
            answer[i][j] = -1

        elif cloud and sky[i][j] == '.':   # 전에 구름이 나온 경우 
            answer[i][j] = time
            time += 1

    print(*answer[i])