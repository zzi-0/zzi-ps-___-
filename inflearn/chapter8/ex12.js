/*
- 조합의 경우수(메모이제이션)

자연수 N을 입력하면 N!값을 구하세요. N! = n*(n-1)*(n-2)*.....*2*1입니다. 
만약 N=5라면 5!=5*4*3*2*1=120입니다.

▣ 입력설명
첫째 줄에 자연수 n(3<=n<=33)과 r(0<=r<=n)이 입력됩니다.

▣ 출력설명
첫째 줄에 조합수를 출력합니다.
*/

function solution(n, r) {
  let dy = Array.from(Array(35), () => Array(35).fill(0));
  function dfs(n, r) {
    if (dy[n][r] > 0) return dy[n][r];
    if (n === r || r === 0) return 1;
    else return (dy[n][r] = dfs(n - 1, r - 1) + dfs(n - 1, r));
  }
  return dfs(n, r);
}

console.log(solution(33, 19));
