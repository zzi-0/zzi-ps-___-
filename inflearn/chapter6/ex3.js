/*
- 크레인 인형뽑기(카카오 기출)
*/

const solution = (array, order) => {
  let stack = [];
  let answer = 0;
  for (let x of order) {
    for (let i = 0; i < array.length; i++) {
      if (array[i][x - 1] !== 0) {
        stack.push(array[i][x - 1]);
        array[i][x - 1] = 0;
        if (stack[stack.length - 1] === stack[stack.length - 2]) {
          stack.pop();
          stack.pop();
          answer = 2 + answer;
        }
        break;
      }
    }
  }

  return answer;
};

console.log(
  solution(
    [
      [0, 0, 0, 0, 0],
      [0, 0, 1, 0, 3],
      [0, 2, 5, 0, 1],
      [4, 2, 4, 4, 2],
      [3, 5, 1, 3, 1],
    ],
    [1, 5, 3, 5, 1, 2, 1, 4]
  )
);
