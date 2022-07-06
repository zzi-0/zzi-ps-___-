function solution(arr, divisor) {
    const answer = arr.filter((num) => num % divisor === 0).sort((a, b) => a - b);

    return answer.length === 0 ? [-1] : answer;
}

console.log(solution([3, 2, 6], 10));
