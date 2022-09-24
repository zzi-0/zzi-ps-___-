function solution(n, s) {
    let answer = [-1];
    const combination = Array.from({ length: n }, () => 0);

    const remainder = s % n;
    const quotient = (s - remainder) / n;

    if (!quotient) return answer;

    for (let i = 0; i < n; i++) {
        combination[i] = quotient;
    }

    if (remainder) {
        for (let i = 0; i < remainder; i++) {
            combination[i] += 1;
        }
    }

    return combination;
}

console.log(solution(4, 99));
