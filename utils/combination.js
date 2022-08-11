// 조합
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

// [ [ 1, 2 ], [ 1, 3 ], [ 1, 4 ], [ 2, 3 ], [ 2, 4 ], [ 3, 4 ] ]
console.log(solution(4, 2));

// 중복조합
function solution2(n, m) {
    let answer = [];
    let arr = [];
    function dfs(v, k) {
        if (v === m) answer.push([...arr]);
        else {
            for (let i = k; i <= n; i++) {
                arr[v] = i;
                dfs(v + 1, i);
            }
        }
    }
    dfs(0, 1);
    return answer;
}

// [[ 1, 1 ], [ 1, 2 ], [ 1, 3 ], [ 1, 4 ],[ 2, 2 ], [ 2, 3 ],[ 2, 4 ], [ 3, 3 ],[ 3, 4 ], [ 4, 4 ]]
console.log(solution2(4, 2));
