n = int(input())



for i in range(n):
    testcase = list(input())
    direction = 1  # 방향 정의 1 = 위쪽, 2 = 오른쪽 , 3 = 아래쪽, 4 = 왼쪽
    x = 0
    y = 0
    # 이동경로 배열로 저장해 최소값 최대값 찾아서 넓이 구하기 위함
    xArr = [0]  
    yArr = [0] 
    for j in testcase:
        if j == "L":
            direction -= 1
            if direction == 0:
                direction = 4
            
        elif j == "R" :
            direction += 1
            if direction == 5:
                direction = 1
            
        else:
            if j == "F" and direction == 1: 
                y += 1
                yArr.append(y)
            elif j == "B" and direction == 1: 
                y -= 1
                yArr.append(y)
            elif j == "F" and direction == 2: 
                x += 1
                xArr.append(x)
            elif j == "B" and direction == 2: 
                x -= 1
                xArr.append(x)
            elif j == "F" and direction == 3: 
                y -= 1
                yArr.append(y)
            elif j == "B" and direction == 3: 
                y += 1
                yArr.append(y)
            elif j == "F" and direction == 4: 
                x -= 1
                xArr.append(x)
            elif j == "B" and direction == 4: 
                x += 1
                xArr.append(x)

    print((max(xArr) - min(xArr)) * (max(yArr) - min(yArr)))