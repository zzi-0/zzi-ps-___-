function solution(rc, operations) {
    let answer = Array.from(Array(rc.length), () => Array(rc[0].length).fill(0));
    operations.forEach((operation) => {
        if (operation === 'Rotate') {
            for (let i = 0; i < rc.length; i++) {
                for (let j = 0; j < rc[0].length; j++) {
                    //오른쪽으로 이동
                    if (i === 0) {
                        if (j === 0) {
                            answer[i][j] = rc[i + 1][j];
                        } else {
                            answer[i][j] = rc[i][j - 1];
                        }
                    }
                    // 왼쪽으로 이동
                    else if (i === rc.length - 1) {
                        if (j === rc[0].length - 1) {
                            answer[i][j] = rc[i - 1][j];
                        } else {
                            answer[i][j] = rc[i][j + 1];
                        }
                    }
                    // 아래쪽으로 이동
                    else if (j === rc[0].length - 1) {
                        if (i > 0 && i < rc.length - 1) {
                            answer[i][j] = rc[i - 1][j];
                        }
                    }
                    // 위쪽으로 이동
                    else if (j === 0) {
                        if (i > 0 && i < rc.length - 1) {
                            answer[i][j] = rc[i + 1][j];
                        }
                    }
                }
            }
            for (let i = 0; i < rc.length; i++) {
                for (let j = 0; j < rc[0].length; j++) {
                    if (answer[i][j] === 0) {
                        answer[i][j] = rc[i][j];
                    }
                }
            }
        }

        if (operation === 'ShiftRow') {
            for (let i = 0; i < rc.length; i++) {
                if (i === 0) {
                    answer[i] = rc[rc.length - 1];
                } else {
                    answer[i] = rc[i - 1];
                }
            }
        }
        rc = answer.map((arr) => arr.slice());
    });
    return answer;
}

console.log(
    solution(
        [
            [1, 2, 3, 4],
            [5, 6, 7, 8],
            [9, 10, 11, 12],
            [13, 14, 15, 16],
            [17, 18, 19, 20],
        ],
        ['Rotate']
    )
);
