/*
- 봉우리
지도 정보가 N*N 격자판에 주어집니다. 각 격자에는 그 지역의 높이가 쓰여있습니다. 
각 격자 판의 숫자 중 자신의 상하좌우 숫자보다 큰 숫자는 봉우리 지역입니다. 봉우리 지역이 몇 개 있는 지 알아내는 프로그램을 작성하세요.
격자의 가장자리는 0으로 초기화 되었다고 가정한다.

▣ 입력설명
첫 줄에 자연수 N이 주어진다.(1<=N<=50)
두 번째 줄부터 N줄에 걸쳐 각 줄에 N개의 자연수가 주어진다. 각 자연수는 100을 넘지 않는다.

▣ 출력설명
봉우리의 개수를 출력하세요.
*/

const solution = (number, array) => {
  let result = 0;
  for (let i = 0; i < number; i++) {
    for (let j = 0; j < number; j++) {
      let flag = 0;
      if (i - 1 >= 0 && array[i - 1][j] > array[i][j]) {
        flag = 1;
      }
      if (i + 1 < number && array[i + 1][j] > array[i][j]) {
        flag = 1;
      }
      if (j - 1 >= 0 && array[i][j - 1] > array[i][j]) {
        flag = 1;
      }
      if (j + 1 < number && array[i][j + 1] > array[i][j]) {
        flag = 1;
      }
      if (flag === 0) result++;
    }
  }
  return result;
};

const array = [
  [5, 3, 7, 2, 3],
  [3, 7, 1, 6, 1],
  [7, 2, 5, 3, 4],
  [4, 3, 6, 4, 1],
  [8, 7, 3, 5, 2],
];
console.log(solution(5, array));
