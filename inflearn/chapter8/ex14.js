/*
- 조합 구하기

1부터 N까지 번호가 적힌 구슬이 있습니다. 이중 M개를 뽑는 방법의 수를 출력하는 프로그램을 작성하세요.

▣ 입력설명
첫 번째 줄에 자연수 N(3<=N<=10)과 M(2<=M<=N) 이 주어집니다.

▣ 출력설명
첫 번째 줄에 결과를 출력합니다. 맨 마지막 총 경우의 수를 출력합니다. 출력순서는 사전순으로 오름차순으로 출력합니다.

 */
function solution(n, m) {
    let answer = [];
    let arr = [];
    function dfs(v, k) {
        if (v === m) answer.push([...arr]);
        else {
            for (let i = k; i <= n; i++) {
                arr[v] = i;
                dfs(v + 1, i + 1);
            }
        }
    }
    dfs(0, 1);
    return answer;
}

console.log(solution(4, 2));
