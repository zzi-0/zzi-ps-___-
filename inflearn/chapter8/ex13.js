/*
- 수열 추측하기

1부터 N까지 번호가 적힌 구슬이 있습니다.
이중 M개를 뽑는 방법의 수를 출력하는 프로그램을 작성하세요.

▣ 입력설명
첫째 줄에 두개의 정수 N(1≤N≤10)과 F가 주어진다. 
N은 가장 윗줄에 있는 숫자의 개수를 의 미하며 F는 가장 밑에 줄에 있는 수로 1,000,000 이하이다.

▣ 출력설명
첫째 줄에 삼각형에서 가장 위에 들어갈 N개의 숫자를 빈 칸을 사이에 두고 출력한다. 
답이 존재 하지 않는 경우는 입력으로 주어지지 않는다.
*/

function solution(n, r) {
  let answer;
  let flag = 0;
  let dy = Array.from(Array(11), () => Array(11).fill(0));
  let check = Array.from({ length: n + 1 }, () => 0);
  let b = Array.from({ length: n }, () => 0);
  let p = Array.from({ length: n }, () => 0);
  function combination(n, r) {
    if (dy[n][r] > 0) return dy[n][r];
    if (n === r || r === 0) return 1;
    else return (dy[n][r] = combination(n - 1, r - 1) + combination(n - 1, r));
  }
  function dfs(L, sum) {
    if (flag) return;
    if (L === n && sum === r) {
      answer = p.slice();
      flag = 1;
    } else {
      for (let i = 1; i <= n; i++) {
        if (check[i] === 0) {
          check[i] = 1;
          p[L] = i;
          dfs(L + 1, sum + b[L] * p[L]);
          check[i] = 0;
        }
      }
    }
  }
  for (let i = 0; i < n; i++) {
    b[i] = combination(n - 1, i);
  }
  dfs(0, 0);
  return answer;
}

console.log(solution(4, 16));
