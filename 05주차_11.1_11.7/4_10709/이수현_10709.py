# 기상캐스터

h, w = map(int, input().split())
weather = [input() for _ in range(h)]
weather_check = [[0] * w for i in range(h)]     # 구름이 오는 지 예측
ac = False      # 'c' 등장 체크
count = 1

for i in range(h):
    for j in range(w):
        # 구름이 뜨지 않을 경우
        if ac == False and weather[i][j] == '.':
            weather_check[i][j] = -1

        elif weather[i][j] == 'c':
            ac = True   # 'c' 등장
            count = 1

        # 'c' 만남
        else:
            weather_check[i][j] = count
            count += 1

    # 초기화
    ac = False
    count = 1

# 출력
for i in range(h):
    for j in range(w):
        print(weather_check[i][j], end=' ')
    print()