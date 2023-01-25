function solution(maps) {
  // 1. 남동북서 기준
  const dy = [1, 0, -1, 0];
  const dx = [0, 1, 0, -1];
  const row = maps.length;
  const col = maps[0].length;

  // 2.
  const visitCount = [...maps].map((r) => r.map((c) => 1));

  // 3.
  const queue = [[0, 0]]; //시작점

  // 4.
  while (queue.length) {
    const [y, x] = queue.shift();

    // 5.
    for (let i = 0; i < 4; i++) {
      const ny = y + dy[i];
      const nx = x + dx[i];

      // 6.
      if (ny >= 0 && nx >= 0 && ny < row && nx < col) {
        // 7.
        if (maps[ny][nx] === 1 && visitCount[ny][nx] === 1) {
          visitCount[ny][nx] = visitCount[y][x] + 1;
          queue.push([ny, nx]);
        }
      }
    }
  }

  return visitCount[row - 1][col - 1] === 1 ? -1 : visitCount[row - 1][col - 1];
}
