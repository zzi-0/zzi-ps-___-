function solution(numbers) {
    let answer = 0;
    const numArray = Array.from({ length: 9 }, (v, i) => i + 1);

    for (const number of numArray) {
        if (!numbers.includes(number)) {
            answer += number;
        }
    }
    return answer;
}
console.log(solution([1, 2, 3, 4, 6, 7, 8, 0]));
