stair_num = int(input())
stair = []

stair.append(0)
for _ in range(stair_num):
    stair.append(int(input()))

dp = []
dp = [0] * (stair_num + 1)

if stair_num == 1 :
    dp[1] = stair[1]
elif stair_num == 2 :
    dp[1] = stair[1]
    dp[2] = max(stair[1] + stair[2], stair[2])
else:
    dp[1] = stair[1]
    dp[2] = max(stair[1] + stair[2], stair[2])
    dp[3] = max(stair[1]+stair[3], stair[2]+stair[3])
    # print('d[1]' + str(dp[1]))
    # print('d[2]' + str(dp[2]))
    # print('d[3]' + str(dp[3]))

    for i in range(4,stair_num+1) :
        dp[i] = max(dp[i-2]+stair[i], dp[i-3]+stair[i-1]+stair[i])      # 왜  dp[i-3]+stair[i-1]+stair[i] stair 1인지 이해하기
        # print('d['+str(i)+']' + str(dp[i]))

print(dp[stair_num])

# ,  dp[i-3]+dp[i-2]