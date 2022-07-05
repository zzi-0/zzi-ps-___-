// https://programmers.co.kr/learn/courses/30/lessons/42576
function solution(participant, completion) {
    participant.sort();
    completion.sort();

    for (let i in participant) {
        if (participant[i] !== completion[i]) return participant[i];
    }
}

console.log(solution(['leo', 'kiki', 'eden'], ['eden', 'kiki']));
