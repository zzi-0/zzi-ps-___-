/*
- 두 배열 합치기

오름차순으로 정렬이 된 두 배열이 주어지면 두 배열을 오름차순으로 합쳐 출력하는 프로그램 을 작성하세요.

▣ 입력설명
첫 번째 줄에 첫 번째 배열의 크기 N(1<=N<=100)이 주어집니다. 두 번째 줄에 N개의 배열 원소가 오름차순으로 주어집니다.
세 번째 줄에 두 번째 배열의 크기 M(1<=M<=100)이 주어집니다. 네 번째 줄에 M개의 배열 원소가 오름차순으로 주어집니다.
각 리스트의 원소는 int형 변수의 크기를 넘지 않습니다.

▣ 출력설명
오름차순으로 정렬된 배열을 출력합니다.
*/

const solution = (n, arr1, m, arr2) => {
  let p1 = 0;
  let p2 = 0;
  let answer = [];
  while (p1 < n && p2 < m) {
    if (arr1[p1] >= arr2[p2]) answer.push(arr2[p2++]);
    else answer.push(arr1[p1++]);
  }
  while (p1 < n) answer.push(arr1[p1++]);
  while (p2 < m) answer.push(arr2[p2++]);
  return answer;
};

console.log(solution(3, [1, 3, 5], 5, [2, 3, 6, 7, 9]));
