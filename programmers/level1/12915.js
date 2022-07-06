function solution(strings, n) {
    strings.sort((a, b) => {
        const first = a[n];
        const second = b[n];
        if (first === second) return (a > b) - (a < b);
        else return (first > second) - (first < second);
    });
    return strings;
}

console.log(solution(['sun', 'bed', 'car'], 1));
