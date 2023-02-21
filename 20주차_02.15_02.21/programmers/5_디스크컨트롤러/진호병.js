function solution(jobs) {
  let j = 0;
  let time = 0;
  let sum = 0;
  let priorityQueue = [];
  jobs.sort((a, b) => a[0] - b[0]);

  while (jobs.length > j || priorityQueue.length !== 0) {
    console.log(priorityQueue);
    if (jobs.length > j && time >= jobs[j][0]) {
      priorityQueue.push(jobs[j++]);
      priorityQueue.sort((a, b) => {
        return a[1] - b[1];
      });
      continue;
    }
    if (priorityQueue.length !== 0) {
      time += priorityQueue[0][1];
      sum += time - priorityQueue[0][0];

      priorityQueue.shift();
    } else {
      time = jobs[j][0];
    }
  }

  return Math.floor(sum / jobs.length);
}
