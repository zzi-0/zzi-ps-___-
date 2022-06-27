/*
이진트리 순회(깊이우선탐색)

전위순회 출력 : 1 2 4 5 3 6 7 
중위순회 출력 : 4 2 5 1 6 3 7 
후위순회 출력 : 4 5 2 6 7 3 1

*/

function solution(number) {
  let answer = "";
  function dfs(v) {
    if (v > 7) return;
    else {
      // console.log(v); -> 전위순회
      dfs(2 * v);
      // console.log(v); -> 중위순회
      dfs(2 * v + 1);
      // console.log(v); -> 후위순회
    }
  }
  dfs(number);
  return answer;
}

console.log(solution(1));
