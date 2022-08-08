function solution(s) {
    const array = s.split(' ');
    return Math.min(...array) + ' ' + Math.max(...array);
}

console.log(solution('1 2 3 4'));
