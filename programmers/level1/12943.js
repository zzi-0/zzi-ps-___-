function solution(num) {
    var answer = 0;
    while (num !== 1) {
        if (num % 2 === 0) num = num / 2;
        else if (num % 2 === 1) num = 3 * num + 1;
        answer++;
        if (answer === 500) {
            num = 1;
            answer = -1;
        }
    }
    return answer;
}

console.log(solution(6));
