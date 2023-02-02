function solution(number, k) {
  const stack = [];
  for (let i = 0; i < number.length; i += 1) {
    while (stack[stack.length - 1] < number[i] && k > 0) {
      k -= 1;
      stack.pop();
    }
    stack.push(number[i]);
  }
  stack.splice(number.length - k, k);
  return stack.join("");
}
