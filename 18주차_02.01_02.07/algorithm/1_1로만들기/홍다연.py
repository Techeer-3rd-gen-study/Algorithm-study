# 1로 만들기 
# https://www.acmicpc.net/problem/1463

x=int(input())

dp={1:0}

def rec(n):
    if n in dp.keys():
        return dp[n]
    if (n%3==0) and (n%2==0):
        dp[n]=min(rec(n//3)+1, rec(n//2)+1)
    elif n%3==0:
        dp[n]=min(rec(n//3)+1, rec(n-1)+1)
    elif n%2==0:
        dp[n]=min(rec(n//2)+1, rec(n-1)+1)
    else:
        dp[n]=rec(n-1)+1

    return dp[n]

print(rec(x))
