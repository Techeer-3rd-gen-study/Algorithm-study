function solution(numbers) {
  var answer = [];
  function isPrime(num) {
    if (num <= 1) return false;
    for (let i = 2; i * i <= num; i++) {
      if (num % i === 0) return false;
    }
    return true;
  }

  function numberCombination(arr, current_num) {
    for (let i = 0; i < arr.length; i++) {
      var new_num = current_num + arr[i];
      var copy_arr = [...arr];
      copy_arr.splice(i, 1);
      if (isPrime(+new_num) && !answer.includes(+new_num)) {
        answer.push(+new_num);
      }
      numberCombination(copy_arr, new_num);
    }
  }

  numberCombination([...numbers], "");

  return answer.length;
}
