function solution(jobs) {
    const length = jobs.length;
    let answer = 0;
    let priortyQueue = [];
    let currentTime = 0;
    let responseTime = 0;
    let [requestTime, turnaroundTime] = [0, 0];
    jobs.sort((a, b) => {
        if (a[0] === b[0]) return a[1] - b[1];
        return a[0] - b[0];
    });

    while (jobs.length || priortyQueue.length) {
        if (priortyQueue.length) {
            [requestTime, turnaroundTime] = priortyQueue.shift();
            responseTime = currentTime + turnaroundTime;
            answer += responseTime - requestTime;
            currentTime = responseTime;
        } else {
            [requestTime, turnaroundTime] = jobs.shift();
            responseTime = requestTime + turnaroundTime;
            answer += turnaroundTime;
            currentTime = responseTime;
        }

        jobs = jobs.filter((job) => {
            const [requestTime] = job;
            if (requestTime <= responseTime) {
                priortyQueue.push(job);
                priortyQueue.sort((a, b) => a[1] - b[1]);
            }
            return requestTime > responseTime;
        });
    }
    return Math.floor(answer / length);
}

console.log(
    solution([
        [0, 1],
        [1, 2],
        [500, 6],
    ])
);
