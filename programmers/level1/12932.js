function solution(n) {
    return String(n)
        .split('')
        .map((number) => parseInt(number))
        .reverse();
}

console.log(solution(12345));
