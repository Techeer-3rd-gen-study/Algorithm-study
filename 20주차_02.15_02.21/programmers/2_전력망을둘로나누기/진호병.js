function solution(n, wires) {
  let graph = [...new Array(n + 1)].map((v) => [...new Array(n + 1)].fill(0));
  let visited = [...new Array(n + 1)].map((v) => false);
  let cnt = 0;
  let answer = [];
  let result = [];

  function dfs(start) {
    visited[start] = true;
    for (let i = 0; i < n + 1; i++) {
      if (graph[start][i] === 1 && !visited[i]) {
        dfs(i);
        cnt++;
      }
    }
  }

  for (let i = 0; i < wires.length; i++) {
    let [x, y] = wires[i];
    graph[x][y] = 1;
    graph[y][x] = 1;
  }

  for (let [a, b] of wires) {
    graph[a][b] = 0;
    graph[b][a] = 0;
    for (let i = 1; i < n + 1; i++) {
      if (!visited[i]) {
        cnt++;
        dfs(i);
        answer.push(cnt);
        cnt = 0;
      }
    }
    result.push(Math.abs(answer[0] - answer[1]));
    visited = [...new Array(n + 1)].map((v) => false);
    answer = [];
    graph[a][b] = 1;
    graph[b][a] = 1;
  }

  // console.log(graph);
  return Math.min(...result);
}
