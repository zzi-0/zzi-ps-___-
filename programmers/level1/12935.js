function solution(arr) {
    return arr.filter((number) => number !== Math.min(...arr)).length === 0
        ? [-1]
        : arr.filter((number) => number !== Math.min(...arr));
}

console.log(solution([10]));
