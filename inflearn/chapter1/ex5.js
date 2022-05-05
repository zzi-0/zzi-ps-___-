/*
- 최솟값 구하기

7개의 수가 주어지면 그 숫자 중 가장 작은 수를 출력하는 프로그램을 작성하세요.

▣ 입력설명
첫 번째 줄에 7개의 수가 주어진다.

▣ 출력설명
첫 번째 줄에 가장 작은 값을 출력한다.

*/

const solution = (...number) => {
  return number.sort(function (a, b) {
    return a - b;
  });
};

console.log(solution(1, 15, 42, 81, 7, 24, 56));
