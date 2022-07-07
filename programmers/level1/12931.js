function solution(n) {
    return String(n)
        .split('')
        .reduce((sum, number) => (sum += parseInt(number)), 0);
}

console.log(solution(123));
