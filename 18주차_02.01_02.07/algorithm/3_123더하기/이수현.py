# 1,2,3 더하기
# https://infinitt.tistory.com/249

tk = int(input())
for _ in range(tk):

	n = int(input())
	dp = [0 for _ in range(n+1)]
	if n<3:
		print(n)
	else:
		dp[1] = 1
		dp[2] = 2
		dp[3] = 4
		for i in range(4, n + 1):
			dp[i] = dp[i - 1] + dp[i - 2] + dp[i - 3]
		print(dp[n])