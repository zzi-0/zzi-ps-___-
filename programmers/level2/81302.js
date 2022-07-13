// 맨하튼 거리 3이상 or 파티션이면 ok
const getManhattanDistance = ([x1, y1], [x2, y2]) => {
    return Math.abs(x1 - x2) + Math.abs(y1 - y2);
};

function solution(places) {
    var answer = [1, 1, 1, 1, 1];

    for (let n = 0; n < places.length; n++) {
        let pIndex = [];
        let xIndex = [];
        for (let i = 0; i < places[n].length; i++) {
            for (let j = 0; j < places[n][i].length; j++) {
                if (places[n][i][j] === 'P') pIndex.push([i, j]);
                if (places[n][i][j] === 'X') xIndex.push([i, j]);
            }
        }
        for (let i = 0; i < pIndex.length; i++) {
            for (let j = i + 1; j < pIndex.length; j++) {
                if (getManhattanDistance(pIndex[i], pIndex[j]) === 1) {
                    // 검증할 필요없이 거리두기 안한것임
                    answer[n] = 0;
                    break;
                } else if (getManhattanDistance(pIndex[i], pIndex[j]) === 2) {
                    // 거리 두기 안한것인데 검증해야함
                    const [x1, y1] = pIndex[i];
                    const [x2, y2] = pIndex[j];
                    if (y1 === y2) {
                        const a = [Math.abs(x1 + x2) / 2, y1];
                        if (xIndex.some((x) => x.every((v, i) => v === a[i]))) continue;
                        else {
                            answer[n] = 0;
                            break;
                        }
                    } else if (x1 === x2) {
                        const a = [x1, Math.abs(y1 + y2) / 2];
                        if (xIndex.some((x) => x.every((v, i) => v === a[i]))) continue;
                        else {
                            answer[n] = 0;
                            break;
                        }
                    } else {
                        const a = [x1, y2];
                        const b = [x2, y1];
                        if (
                            xIndex.some((x) => x.every((v, i) => v === a[i])) &&
                            xIndex.some((x) => x.every((v, i) => v === b[i]))
                        )
                            continue;
                        else {
                            answer[n] = 0;
                            break;
                        }
                    }
                } else continue;
            }
        }
    }

    return answer;
}

console.log(
    solution([
        ['PPOOP', 'OXXOX', 'OPXPX', 'OOXOX', 'POXXP'],
        ['POOPX', 'OXPXP', 'PXXXO', 'OXXXO', 'OOOPP'],
        ['PXOPX', 'OXOXP', 'OXPOX', 'OXXOP', 'PXPOX'],
        ['POOXX', 'XPOOX', 'OOOXX', 'OXOOX', 'OOOOO'],
        ['PXPXP', 'XPXPX', 'PXPXP', 'XPXPX', 'PXPXP'],
    ])
);
