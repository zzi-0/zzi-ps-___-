/*
- 부분집합 구하기(DFS)

자연수 N이 주어지면 1부터 N까지의 원소를 갖는 집합의 부분집합을 모두 출력하는 프로그램 을 작성하세요.

▣ 입력설명
첫 번째 줄에 자연수 N(1<=N<=10)이 주어집니다.

▣ 출력설명
첫 번째 줄부터 각 줄에 하나씩 부분집합을 아래와 출력예제와 같은 순서로 출력한다. 단 공집합은 출력하지 않습니다.
*/

function solution(number) {
    let answer = [];
    let check = Array.from({ length: number + 1 }, () => 0);
    function dfs(v) {
        if (v === number + 1) {
            let tmp = '';
            for (let i = 0; i <= number; i++) {
                if (check[i] === 1) tmp += i + ' ';
            }
            answer.push(tmp.trim());
        } else {
            check[v] = 1;
            dfs(v + 1);
            check[v] = 0;
            dfs(v + 1);
        }
    }
    dfs(1);
    return answer;
}

console.log(solution(3));
