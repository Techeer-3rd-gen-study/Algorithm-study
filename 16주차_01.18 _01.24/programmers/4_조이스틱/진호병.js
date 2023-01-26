function solution(name) {
  let alphabetMove = 0;
  let index = name.length - 1;

  for (let i = 0; i < name.length; i++) {
    var word = name[i].charCodeAt();
    if (word > 78) {
      alphabetMove += 91 - word;
    } else {
      alphabetMove += word - 65;
    }

    let idx = i + 1;

    // 연속되는 A의 개수 count
    while (idx < name.length && name[idx] === "A") {
      idx++;
    }

    index = Math.min(
      index,
      i * 2 + name.length - idx,
      i + 2 * (name.length - idx)
    );
  }

  return alphabetMove + index;
}
