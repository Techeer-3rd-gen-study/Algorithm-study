
#11052 

n = int(input())

card = [0] + list(map(int,input().split()))

dp = [0] * 1001 #dp 배열에는 해당 인덱스 = 카드의 갯수만큼 뽑았을 때 최대사용 금액을 저장함

for i in range(1,n+1):
  for j in range(1,i+1):
    dp[i] = max(dp[i],dp[i-j]+card[j]) # 이전까지의 계산 중 최대값은 dp[i-j]에 이미 저장되어있음 

print(dp[n])


