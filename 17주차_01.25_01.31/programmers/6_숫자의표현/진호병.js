function solution(n) {
  var answer = 1;
  for (let i = 1; i <= n / 2; i++) {
    var sum = 0;
    for (let j = i; j <= n / 2 + 1; j++) {
      sum += j;
      if (sum === n) {
        answer++;
        break;
      }
      if (sum > n) {
        break;
      }
    }
  }
  return answer;
}
