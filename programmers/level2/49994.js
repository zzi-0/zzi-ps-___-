//17:00
function solution(dirs) {
    let currentCoordinate = [0, 0];
    const loadArr = [];

    for (let i = 0; i < dirs.length; i++) {
        const [x, y] = currentCoordinate;
        if (x === 5 && dirs[i] === 'R') continue;
        if (x === -5 && dirs[i] === 'L') continue;
        if (y === 5 && dirs[i] === 'U') continue;
        if (y === -5 && dirs[i] === 'D') continue;
        if (dirs[i] === 'U') {
            currentCoordinate = [x, y + 1];
            const newY = y + 1;
            loadArr.push(x + '' + newY + '' + x + '' + y);
            loadArr.push(x + '' + y + '' + x + '' + newY);
        }
        if (dirs[i] === 'D') {
            currentCoordinate = [x, y - 1];
            const newY = y - 1;
            loadArr.push(x + '' + y + '' + x + '' + newY);
            loadArr.push(x + '' + newY + '' + x + '' + y);
        }
        if (dirs[i] === 'R') {
            currentCoordinate = [x + 1, y];
            const newX = x + 1;
            loadArr.push(x + '' + y + '' + newX + '' + y);
            loadArr.push(newX + '' + y + '' + x + '' + y);
        }
        if (dirs[i] === 'L') {
            currentCoordinate = [x - 1, y];
            const newX = x - 1;
            loadArr.push(x + '' + y + '' + newX + '' + y);
            loadArr.push(newX + '' + y + '' + x + '' + y);
        }
    }
    return new Set([...loadArr]).size / 2;
}

console.log(solution('DUUUUDDDDDD'));
