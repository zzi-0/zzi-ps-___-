function solution(citations) {
    let answer = 0;
    let max = Math.max(...citations);
    while (max > 0) {
        let above = 0;
        citations.forEach((citation) => {
            if (citation >= max) above++;
        });
        if (above >= max) {
            answer = max;
            break;
        }
        max--;
    }
    return answer;
}
console.log(solution([0, 1, 1]));
