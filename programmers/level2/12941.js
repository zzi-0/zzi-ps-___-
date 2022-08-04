function solution(a, b) {
    var answer = 0;

    a.sort((a, b) => a - b);
    b.sort((a, b) => b - a);
    while (a.length) {
        answer += a.shift() * b.shift();
    }

    return answer;
}

console.log(solution([1, 4, 2], [5, 4, 4]));
