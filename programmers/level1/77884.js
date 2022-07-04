function getPrimeCount(num) {
    let count = 0;
    for (let i = 1; i <= num; i++) {
        if (num % i === 0) count++;
    }
    return count;
}

function solution(left, right) {
    var answer = 0;
    for (let i = left; i <= right; i++) {
        if (getPrimeCount(i) % 2 === 0) answer = answer + i;
        else answer = answer - i;
    }
    return answer;
}

console.log(solution(13, 17));
