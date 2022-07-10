function solution(people, limit) {
    var answer = 0;
    let beforeAnswer = 0;

    people.sort((a, b) => b - a);
    while (people.length) {
        people.sort((a, b) => b - a);
        for (let i = 0; i < people.length - 1; i++) {
            if (people[i] + people[i + 1] <= limit) {
                answer++;
                people.splice(i, 2);
                i--;
                i--;
            }
        }
        if (beforeAnswer === answer) break;
        beforeAnswer = answer;
    }
    answer += people.length;
    return answer;
}

console.log(solution([70, 50, 80, 50], 100));
