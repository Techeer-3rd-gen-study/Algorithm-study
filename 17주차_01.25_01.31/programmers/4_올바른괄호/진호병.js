function solution(s) {
  const stack = [];
  var answer = true;

  // 이건 괜찮은데 s[0]이 ) 인지 검사하는 로직을 추가하면 시간 초과가 난다. 왜지 ?
  if (s.length % 2 !== 0) {
    return false;
  }

  for (let i = 0; i < s.length; i++) {
    if (stack[stack.length - 1] === "(" && s[i] === ")") {
      stack.pop();
    } else {
      stack.push(s[i]);
    }
  }

  if (stack.length !== 0) {
    answer = false;
  }

  return answer;
}
