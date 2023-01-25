function solution(array, commands) {
  var answer = [];
  commands.forEach((item, index) => {
    var sliceArr = array.slice(item[0] - 1, item[1]);
    var sortArr = sliceArr.sort((a, b) => a - b);
    answer.push(sortArr[item[2] - 1]);
  });
  return answer;
}
