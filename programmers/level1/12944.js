function solution(arr) {
    return arr.reduce((sum, num) => (sum += num)) / arr.length;
}

console.log(solution([1, 2, 3, 4]));
