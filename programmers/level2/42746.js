//10:15 -
function solution(numbers) {
    const answer = numbers
        .map((a) => String(a))
        .sort((a, b) => b + a - (a + b))
        .join('');
    return answer[0] === '0' ? '0' : answer;
}

console.log(solution([3, 30, 34, 5, 9, 68, 3]));

('9 5 34 3 30 304 30 300');
