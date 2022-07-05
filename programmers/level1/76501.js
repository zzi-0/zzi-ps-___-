function solution(absolutes, signs) {
    return absolutes.reduce((acc, absolute, idx) => (acc += signs[idx] ? absolute : -absolute), 0);
}
console.log(solution([4, 7, 12], [true, false, true]));
