function solution(n) {
    let ternary = '';
    while (n > 0) {
        ternary += parseInt(n % 3);
        n = parseInt(n / 3);
    }

    return parseInt(ternary, 3);
}

console.log(solution(45));
