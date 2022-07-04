function solution(N, stages) {
    let answer = [];
    let failureRate = [];

    for (let i = 1; i <= N; i++) {
        let total = 0;
        let failure = 0;
        for (let j = 0; j < stages.length; j++) {
            if (i <= stages[j]) total++;
            if (i === stages[j]) failure++;
        }
        if (total === 0) failureRate.push(0);
        else failureRate.push(failure / total);
    }

    while (answer.length < N) {
        const index = failureRate.indexOf(Math.max(...failureRate));
        answer.push(index + 1);
        failureRate[index] = -1;
    }
    return answer;
}

console.log(solution(4, [4, 4, 4, 4, 4]));
