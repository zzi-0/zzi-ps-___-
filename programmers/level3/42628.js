function solution(operations) {
    let queue = [];
    operations.forEach((operation) => {
        const [a, b] = operation.split(' ');
        if (a === 'I') queue.unshift(b);
        if (a === 'D' && b === '-1') queue = queue.filter((q) => Number(q) !== Math.min(...queue));
        if (a === 'D' && b === '1') queue = queue.filter((q) => Number(q) !== Math.max(...queue));
    });

    if (!queue.length) return [0, 0];
    return [Math.max(...queue), Math.min(...queue)];
}

console.log(solution(['I 16', 'I -5643', 'D -1', 'D 1', 'D 1', 'I 123', 'D -1']));
