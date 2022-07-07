function solution(x) {
    const sum = (x + '').split('').reduce((sum, num) => (sum += +num), 0);
    return x % sum ? false : true;
}

console.log(solution(13));
