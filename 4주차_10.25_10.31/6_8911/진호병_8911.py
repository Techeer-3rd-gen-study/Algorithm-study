n = int(input())

for i in range(n):
    testcase = list(input())
    direction = 1 # 홀수 방향 == y축 이동
    x = 0
    y = 0
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
    # print(max(xArr))
    # print(min(xArr))

    # print(max(yArr))
    # print(min(yArr))

    print((max(xArr) - min(xArr)) * (max(yArr) - min(yArr)))