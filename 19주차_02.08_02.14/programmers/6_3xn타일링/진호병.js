function solution(n) {
  var answer = 0;
  var dp = [0, 3, 11];
  for (let i = 3; i <= n / 2; i++) {
    dp[i] =
      dp.reduce((acc, cur, idx) => {
        if (idx == dp.length - 1) {
          return acc + cur * 3;
        }
        return acc + cur * 2;
      }, 2) % 1000000007;
  }
  return dp[n / 2];
}
