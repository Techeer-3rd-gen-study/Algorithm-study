# @, %, #을 사용한다. @는 3을 곱하고, %는 5를 더하며, #는 7을 빼는 연산자
# 3
# 3 @ %
# 10.4 # % @
# 8 #

t = int(input())

ans = list()

for i in range(t) :
    li = list(input().split())
    num = float(li.pop(0))

    for j in range(len(li)): 
        if li[j] == '@' :
            num *= 3
        elif li[j] == '%':
            num += 5
        elif li[j] == '#':
            num -= 7

    ans.append("{:0.2f}".format(num))

for i in range(len(ans)):
    print(ans[i])

    
   

    