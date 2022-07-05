function solution(a, b) {
    return a.reduce((sum, num, idx) => (sum += b[idx] * num), 0);
}
console.log(solution([1, 2, 3, 4], [-3, -1, 0, 2]));
