/*
- 경로 탐색(인접행렬)

▣ 입력설명
첫째 줄에는 정점의 수 N(1<=N<=20)와 간선의 수 M가 주어진다. 
그 다음부터 M줄에 걸쳐 연 결정보가 주어진다.

▣ 출력설명
총 가지수를 출력한다.

*/

function solution(n, array) {
  let answer = 0;
  let graph = Array.from(Array(n + 1), () => Array(n + 1).fill(0));
  let check = Array.from({ length: n + 1 }, () => 0);

  for (let [a, b] of array) {
    graph[a][b] = 1;
  }

  function dfs(L) {
    if (n === L) answer++;
    else {
      for (let i = 1; i <= n; i++) {
        if (graph[L][i] === 1 && check[i] === 0) {
          check[i] = 1;
          dfs(i);
          check[i] = 0;
        }
      }
    }
  }
  check[1] = 1;
  dfs(1);
  return answer;
}

console.log(
  solution(5, [
    [1, 2],
    [1, 3],
    [1, 4],
    [2, 1],
    [2, 3],
    [2, 5],
    [3, 4],
    [4, 2],
    [4, 5],
  ])
);
