function solution(s) {
    let tryCount = 0;
    let zeroCount = 0;

    while (s.length > 1) {
        const filterS = s.split('').filter((c) => c === '1');
        const newS = filterS.length.toString(2);
        const sZeroCount = s.length - filterS.length;
        const newSZeroCount = newS.split('').filter((c) => c === 0);
        zeroCount += sZeroCount - newSZeroCount;
        tryCount++;
        s = newS;
    }
    return [tryCount, zeroCount];
}

console.log(solution('110010101001'));
