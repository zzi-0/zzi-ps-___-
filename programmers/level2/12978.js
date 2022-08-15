function solution(n, road, k) {
    var answer = 1;
    let graph = Array.from(Array(n + 1), () => Array(n + 1).fill(0));
    let check = Array.from({ length: n + 1 }, () => 0);
    let check2 = Array.from({ length: n + 1 }, () => 0);

    for (let [a, b, c] of road) {
        if (graph[a][b] === 0 || (graph[a][b] > c && graph[a][b] !== 0)) graph[a][b] = c;
        if (graph[b][a] === 0 || (graph[b][a] > c && graph[b][a] !== 0)) graph[b][a] = c;
    }

    function dfs(L, sum) {
        if (sum > k) return;
        if (sum <= k && sum > 0) {
            if (!check2[L]) answer++;
            check2[L] = 1;
        }
        for (let i = 1; i <= n; i++) {
            if (graph[L][i] !== 0 && check[i] === 0) {
                check[i] = 1;
                dfs(i, sum + graph[L][i]);
                check[i] = 0;
            }
        }
    }
    check[1] = 1;
    dfs(1, 0);

    return answer;
}

console.log(
    solution(
        6,
        [
            [1, 2, 1],
            [1, 3, 2],
            [2, 3, 2],
            [3, 4, 3],
            [3, 5, 2],
            [3, 5, 3],
            [5, 6, 1],
        ],
        4
    )
);
