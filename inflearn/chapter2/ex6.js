/*
- 격자판 최대합
N*N의 격자판이 주어지면 각 행의 합, 각 열의 합, 두 대각선의 합 중 가 장 큰 합을 출력합 니다.

▣ 입력설명
첫 줄에 자연수 N이 주어진다.(1<=N<=50)

두 번째 줄부터 N줄에 걸쳐 각 줄에 N개의 자연수가 주어진다. 각 자연수는 100을 넘지 않는 다.
▣ 출력설명 최대합을 출력합니다.
*/

const solution = (number, array) => {
  let maxSum = 0;
  let sum1 = 0;
  let sum2 = 0;

  for (let i = 0; i < number; i++) {
    sum1 = 0;
    sum2 = 0;
    for (let j = 0; j < number; j++) {
      sum1 = sum1 + array[i][j];
      sum2 = sum2 + array[j][i];
    }
    if (maxSum < sum1) maxSum = sum1;
    if (maxSum < sum2) maxSum = sum2;
  }

  sum1 = 0;
  sum2 = 0;
  for (let i = 0; i < number; i++) {
    sum1 = sum1 + array[i][i];
    sum2 = sum2 + array[i][number - i - 1];
  }
  if (maxSum < sum1) maxSum = sum1;
  if (maxSum < sum2) maxSum = sum2;
  return maxSum;
};

const array = [
  [10, 13, 10, 12, 15],
  [12, 39, 30, 23, 11],
  [11, 25, 50, 53, 15],
  [19, 27, 29, 37, 27],
  [19, 13, 30, 13, 19],
];
console.log(solution(5, array));
