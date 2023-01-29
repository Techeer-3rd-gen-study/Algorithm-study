function solution(n) {
  var count = 0;
  var n_to_binary = [...n.toString(2)];
  n_to_binary.forEach((item) => {
    if (item === "1") {
      count++;
    }
  });

  while (true) {
    var next_count = 0;
    n++;
    var next_binary = [...n.toString(2)];
    next_binary.forEach((item) => {
      if (item === "1") {
        next_count++;
      }
    });
    if (next_count === count) {
      return n;
    }
  }
}
