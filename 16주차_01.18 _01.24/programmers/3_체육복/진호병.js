function solution(n, lost, reserve) {
  var answer = n;
  const arr = [...new Array(n)].map((_, i) => 1);

  lost.forEach((item) => arr[item - 1]--);

  reserve.forEach((item) => arr[item - 1]++);

  for (let i = 0; i < n; i++) {
    if (arr[i] === 0) {
      if (arr[i - 1] === 2) {
        arr[i - 1]--;
        arr[i]++;
      } else if (arr[i + 1] === 2) {
        arr[i]++;
        arr[i + 1]--;
      }
    }
  }

  arr.forEach((item) => {
    if (item === 0) {
      answer--;
    }
  });

  console.log(arr);

  //     lost = lost.sort((a,b)=>a-b);
  //     reserve = reserve.sort((a,b)=>a-b);

  //     lost.forEach(item => {
  //         arr[item-1] = false;
  //     })

  //     lost.forEach(item =>{
  //         reserve = reserve.filter(i => {
  //            if(i != item){
  //                return i;
  //            }
  //         });

  //     })

  //     if (reserve.length !== 0){
  //         reserve.forEach(item => {
  //             if(arr[item-2] === false){
  //                 arr[item-2] = true;
  //             }
  //             else if (arr[item] === false){
  //                 arr[item] = true;
  //             }
  //         });
  //     }

  //     arr.forEach(item => {
  //         if (item === true){
  //             answer++;
  //         }
  //     })
  return answer;
}
