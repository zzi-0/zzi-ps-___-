function solution(rc, operations) {
  let answer = rc.map((v) => [...v]);

  operations.forEach((operation) => {
    let temp = answer.map((v) => [...v]);
    if (operation === "Rotate") {
      for (let i = 0; i < answer.length; i++) {
        for (let j = 0; j < answer[i].length; j++) {
          if (i === 0 && j > 0) {
            temp[i][j] = answer[i][j - 1];
          }
          if (i === answer.length - 1 && j < answer[i].length - 1) {
            temp[i][j] = answer[i][j + 1];
          }
          if (j === 0 && i < answer.length - 1) {
            temp[i][j] = answer[i + 1][j];
          }
          if (j === answer[i].length - 1 && i > 0) {
            temp[i][j] = answer[i - 1][j];
          }
        }
      }
      answer = temp.map((v) => [...v]);
    }
    if (operation === "ShiftRow") {
      let temp = answer.map((v) => [...v]);
      for (let i = 0; i < answer.length; i++) {
        if (i === 0) {
          temp[i] = answer[answer.length - 1];
        } else {
          temp[i] = answer[i - 1];
        }
      }
      answer = temp.map((v) => [...v]);
    }
  });

  return answer;
}

console.log(
  solution(
    [
      [1, 2, 3],
      [4, 5, 6],
      [7, 8, 9],
    ],
    ["Rotate", "ShiftRow"]
  )
);
