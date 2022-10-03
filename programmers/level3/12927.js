function solution(n, works) {
    let answer = 0;
    let remain = n;

    const sum = works.reduce((acc, cur) => acc + cur, 0);
    if (sum <= n) return answer;

    while (remain > 0) {
        works.sort((a, b) => b - a);
        works[0] = works[0] - 1;
        remain--;
    }

    return works.reduce((acc, cur) => acc + cur ** 2, 0);
}

console.log(solution(4, [4, 3, 3]));
