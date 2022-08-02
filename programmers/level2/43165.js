function solution(numbers, target) {
    var answer = 0;
    function dfs(v, sum) {
        if (v === numbers.length) {
            if (sum === target) answer++;
        } else {
            dfs(v + 1, sum + numbers[v]);
            dfs(v + 1, sum - numbers[v]);
        }
    }
    dfs(0, 0);
    return answer;
}

console.log(solution([4, 1, 2, 1], 2));
