function solution(s) {
    if (s.length % 2 === 1) return s.slice(parseInt(s.length / 2), parseInt(s.length / 2) + 1);
    else return s.slice(parseInt(s.length / 2) - 1, parseInt(s.length / 2) + 1);
}

console.log(solution('aavnn'));
