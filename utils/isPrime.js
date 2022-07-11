// 소수인지 검사하는 코드
const isPrime = (num) => {
    if (num === 1 || num === 0) return false;
    for (let i = 2; i < num; i++) {
        if (num % i === 0) return false;
    }
    return true;
};
