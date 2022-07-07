function solution(n, m) {
    let biggerNum = n > m ? n : m;
    let commonDivior = 0;
    let commonMultiple = 0;

    for (let i = 1; i <= biggerNum; i++) {
        if (n % i === 0 && m % i === 0) commonDivior = i;
    }
    commonMultiple = (n * m) / commonDivior;
    return [commonDivior, commonMultiple];
}

console.log(solution(3, 12));
