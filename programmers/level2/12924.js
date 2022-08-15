function solution(n) {
    var answer = 0;
    let arr = [];
    let sum = 0;
    for (let i = 1; i <= n; i++) {
        for (let j = i; j <= n; j++) {
            sum += j;
            arr.push(j);
            if (sum === n) answer++;
            else if (sum >= n) {
                sum = 0;
                arr = [];
                break;
            }
        }
    }
    return answer;
}

console.log(solution(15));
