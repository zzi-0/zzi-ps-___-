// 순열
function solution(n, m) {
    let answer = [];
    let arr = [];
    let check = [];
    function dfs(v) {
        if (v === m) answer.push([...arr]);
        else {
            for (let i = 1; i <= n; i++) {
                if (!check[i]) {
                    arr[v] = i;
                    check[i] = 1;
                    dfs(v + 1);
                    check[i] = 0;
                }
            }
        }
    }
    dfs(0);
    return answer;
}

// [ [ 1, 2 ], [ 1, 3 ], [ 2, 1 ], [ 2, 3 ], [ 3, 1 ], [ 3, 2 ] ]
console.log(solution(3, 2));

// 중복순열
function solution2(n, m) {
    let answer = [];
    let array = Array.from({ length: m }, () => 0);

    function dfs(v) {
        if (v > m) return;
        if (v === m) {
            answer.push([...array]);
        } else {
            for (let i = 1; i <= n; i++) {
                array[v] = i;
                dfs(v + 1);
            }
        }
    }

    dfs(0);

    return answer;
}

// [[ 1, 1 ], [ 1, 2 ],[ 1, 3 ], [ 2, 1 ],[ 2, 2 ], [ 2, 3 ],[ 3, 1 ], [ 3, 2 ],[ 3, 3 ]]
console.log(solution2(3, 2));
