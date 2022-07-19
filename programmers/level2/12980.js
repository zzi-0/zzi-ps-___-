//16:30
function solution(n) {
    let answer = 0;

    while (n) {
        if (n % 2 === 1) {
            n = n - 1;
            answer++;
            if (n === 1) break;
        } else n = Math.floor(n / 2);
    }

    return answer;
}

console.log(solution(5000));
