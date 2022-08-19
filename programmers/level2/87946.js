function solution(k, dungeons) {
    let answer = [];
    let check = Array.from({ length: dungeons.length }, () => 0);

    function dfs(v, remain) {
        if (v === dungeons.length) {
            answer.push(v);
        } else {
            for (let i = 0; i < dungeons.length; i++) {
                if (!check[i]) {
                    const [m, c] = dungeons[i];
                    if (remain >= m && remain >= c) {
                        check[i] = 1;
                        dfs(v + 1, remain - c);
                        check[i] = 0;
                    } else {
                        answer.push(v);
                    }
                }
            }
        }
    }

    dfs(0, k);
    return Math.max(...answer);
}

console.log(
    solution(80, [
        [80, 20],
        [50, 40],
        [30, 20],
    ])
);
