function solution(x, n) {
    var answer = [];

    if (x === 0) for (let i = x; i < n; i++) answer.push(0);
    else if (x < 0) for (let i = x; i >= x * n; i += x) answer.push(i);
    else for (let i = x; i <= x * n; i += x) answer.push(i);

    return answer;
}

console.log(solution(-4, 2));
