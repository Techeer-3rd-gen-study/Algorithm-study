function solution(tickets) {
  tickets.sort(); // 글자순 정렬
  let vis = Array(tickets.length).fill(false);
  var answer = [];
  function dfs(cur, cnt, path) {
    if (cnt === tickets.length) {
      //정렬했으므로 처음오는 경우의 수가 답
      answer = path;
      return true;
    }
    for (let i = 0; i < tickets.length; i += 1) {
      if (vis[i]) continue;
      if (tickets[i][0] === cur) {
        // 출발하는 공항이 같다.
        vis[i] = true;
        if (dfs(tickets[i][1], cnt + 1, [...path, tickets[i][1]])) {
          console.log("asd");
          return true;
        }
        vis[i] = false;
      }
    }

    return false;
  }
  dfs("ICN", 0, ["ICN"]);
  return answer;
}
