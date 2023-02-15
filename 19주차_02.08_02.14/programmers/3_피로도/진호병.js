function solution(k, dungeons) {
  var answer = -1;
  var visited = [...Array(dungeons.length)].map((v) => false);

  function dfs(count, fatigue) {
    if (count > answer) {
      answer = count;
    }
    for (let i = 0; i < dungeons.length; i++) {
      if (!visited[i] && fatigue >= dungeons[i][0]) {
        visited[i] = true;
        dfs(count + 1, fatigue - dungeons[i][1]);
        visited[i] = false;
      }
    }
  }

  dfs(0, k);

  return answer;
}
