function solution(brown, yellow) {
    // 가로 + 세로 = brown/2 + 2
    // 가로 * 세로 = brown + yellow
    const sum = brown + yellow;
    const possibleAnswer = [];
    for (let i = 1; i <= Math.ceil(Math.sqrt(sum)); i++) {
        if (sum % i === 0) possibleAnswer.push([i, sum / i]);
    }
    for (const answer of possibleAnswer) {
        const [a, b] = answer;
        if (a + b === brown / 2 + 2) return a > b ? [a, b] : [b, a];
    }
}

console.log(solution(10, 2));
