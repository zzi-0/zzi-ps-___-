const isPrime = (num) => {
    if (num === 1) return false;
    for (let i = 2; i <= Math.sqrt(num); i++) {
        if (num % i === 0) return false;
    }
    return true;
};

function solution(n, k) {
    let answer = 0;
    let num = n.toString(k);
    num = num.split('0');

    num.forEach((n) => {
        if (n && isPrime(Number(n))) answer++;
    });

    return answer;
}

console.log(solution(1000, 10));
