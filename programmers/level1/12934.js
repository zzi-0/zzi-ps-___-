function solution(n) {
    const squareRoot = Math.sqrt(n);
    if (squareRoot % 1 === 0) return Math.pow(squareRoot + 1, 2);
    else return -1;
}

console.log(solution(31));
