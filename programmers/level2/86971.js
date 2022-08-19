function solution(n, wires) {
    var answer = n;
    let graph = Array.from(Array(n + 1), () => Array(n + 1).fill(0));
    let check = Array.from({ length: n + 1 }, () => 0);
    let count = 1;

    for (let [a, b] of wires) {
        graph[a][b] = 1;
        graph[b][a] = 1;
    }

    function dfs(L) {
        for (let i = 1; i <= n; i++) {
            if (graph[L][i] === 1 && check[i] === 0) {
                check[i] = 1;
                count++;
                dfs(i);
                check[i] = 0;
            }
        }
    }

    for (let [a, b] of wires) {
        graph[a][b] = 0;
        graph[b][a] = 0;

        count = 1;
        check[1] = 1;
        dfs(1);

        graph[a][b] = 1;
        graph[b][a] = 1;
        answer = Math.min(answer, Math.abs(n - count - count));
    }
    return answer;
}

console.log(
    solution(9, [
        [1, 3],
        [2, 3],
        [3, 4],
        [4, 5],
        [4, 6],
        [4, 7],
        [7, 8],
        [7, 9],
    ])
);
