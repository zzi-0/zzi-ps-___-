function solution(n, a, b) {
    var answer = 1;
    let aIndex = Math.ceil(a);
    let bIndex = Math.ceil(b);

    while (n) {
        if (aIndex % 2 === 0 && aIndex - 1 === bIndex) break;
        if (aIndex % 2 !== 0 && aIndex + 1 === bIndex) break;

        a = a / 2;
        b = b / 2;
        aIndex = Math.ceil(a);
        bIndex = Math.ceil(b);
        answer++;
    }

    return answer;
}

console.log(solution(8, 7, 3));
