function solution(numbers) {
  numbers = numbers
    .map((i) => i + "")
    .sort((a, b) => b + a - (a + b))
    .join("");
  return numbers[0] === "0" ? "0" : numbers;
}
