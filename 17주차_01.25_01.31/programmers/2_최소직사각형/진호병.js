function solution(sizes) {
  var answer = 0;
  for (let i = 0; i < sizes.length; i++) {
    if (sizes[i][0] < sizes[i][1]) {
      var shift_item = sizes[i].shift();
      sizes[i].push(shift_item);
    }
  }
  var max1 = 0;
  var max2 = 0;

  for (let i = 0; i < sizes.length; i++) {
    if (max1 < sizes[i][0]) {
      max1 = sizes[i][0];
    }

    if (max2 < sizes[i][1]) {
      max2 = sizes[i][1];
    }
  }

  answer = max1 * max2;
  return answer;
}
