/*
- 중복순열 구하기

1부터 N까지 번호가 적힌 구슬이 있습니다. 이 중 중복을 허락하여 M번을 뽑아 일렬로 나열 하는 방법을 모두 출력합니다.

▣ 입력설명
첫 번째 줄에 자연수 N(3<=N<=10)과 M(2<=M<=N) 이 주어집니다.

▣ 출력설명
첫 번째 줄에 결과를 출력합니다. 맨 마지막 총 경우의 수를 출력합니다. 출력순서는 사전순으로 오름차순으로 출력합니다.
*/

function solution(n, m) {
  let answer = [];
  let tmp = Array.from({ length: m }, () => 0);
  function dfs(v) {
    if (v === m) {
      answer.push(tmp.slice());
    } else {
      for (let i = 1; i <= n; i++) {
        tmp[v] = i;
        dfs(v + 1);
      }
    }
  }
  dfs(0);
  return answer;
}

console.log(solution(3, 2));
