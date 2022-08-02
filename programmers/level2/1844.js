function solution(maps) {
    let queue = [];
    let dx = [-1, 0, 1, 0];
    let dy = [0, 1, 0, -1];
    const n = maps.length - 1;
    const m = maps[0].length - 1;
    queue.push([0, 0, 1]);
    maps[0][0] = 0;

    while (queue.length) {
        let shiftItem = queue.shift();

        let [x, y, count] = shiftItem;
        for (let i = 0; i < 4; i++) {
            let nx = x + dx[i];
            let ny = y + dy[i];
            if (nx >= 0 && nx <= n && ny >= 0 && ny <= m && maps[nx][ny] === 1) {
                if (nx === n && ny === m) return count + 1;
                queue.push([nx, ny, count + 1]);
                maps[nx][ny] = 0;
            }
        }
    }
    return -1;
}

console.log(
    solution([
        [1, 0, 1, 1, 1],
        [1, 0, 1, 0, 1],
        [1, 0, 1, 1, 1],
        [1, 1, 1, 0, 1],
        [0, 0, 0, 0, 1],
    ])
);
