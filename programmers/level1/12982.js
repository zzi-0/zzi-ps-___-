function solution(d, budget) {
    var answer = 0;
    let sum = 0;
    d.sort((a, b) => a - b);
    for (const money of d) {
        sum += money;
        if (sum === budget) {
            answer++;
            break;
        } else if (sum > budget) break;
        else answer++;
    }
    return answer;
}
console.log(solution([1, 3, 2, 5, 4], 9));
