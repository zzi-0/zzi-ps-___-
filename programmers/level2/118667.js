// 13:40
function solution(queue1, queue2) {
    let answer = 0;
    let queue = [];
    const len = queue1.length;
    const queue1Sum = queue1.reduce((acc, q) => (acc += q), 0);
    const queue2Sum = queue2.reduce((acc, q) => (acc += q), 0);
    const sum = queue1Sum + queue2Sum;
    if (sum % 2 !== 0) return -1;

    const queue1Pop = (q1, q2) => {
        const tmpQueue1 = [...q1];
        const tmpQueue2 = [...q2];
        const q = tmpQueue1.shift();
        tmpQueue2.push(q);

        const queue1Sum = tmpQueue1.reduce((acc, q) => (acc += q), 0);
        const queue2Sum = tmpQueue2.reduce((acc, q) => (acc += q), 0);
        return [[...tmpQueue1], [...tmpQueue2], queue1Sum, queue2Sum];
    };

    const queue2Pop = (q1, q2) => {
        const tmpQueue1 = [...q1];
        const tmpQueue2 = [...q2];
        const q = tmpQueue2.shift();
        tmpQueue1.push(q);

        const queue1Sum = tmpQueue1.reduce((acc, q) => (acc += q), 0);
        const queue2Sum = tmpQueue2.reduce((acc, q) => (acc += q), 0);
        return [[...tmpQueue1], [...tmpQueue2], queue1Sum, queue2Sum];
    };

    queue.push([0, queue1, queue2, queue1Sum, queue2Sum]);
    while (queue.length) {
        const [count, q1, q2, q1sum, q2sum] = queue.shift();
        if (q1sum === q2sum) return count;
        for (let nv of [queue1Pop, queue2Pop]) {
            queue.push([count + 1, ...nv(q1, q2)]);
        }
        answer++;
        if (count >= Math.pow(2, len)) return -1;
    }

    return answer;
}

console.log(solution([1, 1], [1, 5]));
