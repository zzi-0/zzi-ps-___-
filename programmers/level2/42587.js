function solution(priorities, location) {
    let priorityQueue = [];
    let queue = [];
    let answer = 0;

    priorities.forEach((priority, index) => {
        priorityQueue.push([priority, index]);
    });

    while (priorityQueue.length) {
        const [elePriority, eleIndex] = priorityQueue.shift();
        const hasHighPriority = priorityQueue.some((priorityInfo) => {
            const [priority, index] = priorityInfo;
            return priority > elePriority;
        });
        if (hasHighPriority) priorityQueue.push([elePriority, eleIndex]);
        else {
            queue.push([elePriority, eleIndex]);
        }
    }
    queue.forEach((queueEle, i) => {
        const [priority, index] = queueEle;
        if (index === location) answer = i;
    });
    return answer + 1;
}

console.log(solution([1, 1, 9, 1, 1, 1], 0));
