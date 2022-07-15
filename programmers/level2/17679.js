function solution(m, n, board) {
    let popIndex = [];
    board = board.map((v) => v.split(''));
    while (popIndex) {
        popIndex = [];

        for (let i = 0; i < board.length - 1; i++) {
            for (let j = 0; j < board[i].length - 1; j++) {
                if (
                    board[i][j] &&
                    board[i][j] === board[i][j + 1] &&
                    board[i][j] === board[i + 1][j] &&
                    board[i][j] === board[i + 1][j + 1]
                ) {
                    popIndex.push([i, j]);
                }
            }
        }

        if (popIndex.length === 0) break;

        for (const i of popIndex) {
            const [a, b] = i;
            board[a][b] = 0;
            board[a + 1][b] = 0;
            board[a][b + 1] = 0;
            board[a + 1][b + 1] = 0;
        }

        for (let i = m - 1; i > 0; i--) {
            if (!board[i].some((v) => !v)) continue;

            for (let j = 0; j < n; j++) {
                for (let k = i - 1; k >= 0 && !board[i][j]; k--) {
                    if (board[k][j]) {
                        board[i][j] = board[k][j];
                        board[k][j] = 0;
                        break;
                    }
                }
            }
        }
    }
    return [].concat(...board).filter((v) => !v).length;
}

console.log(solution(4, 5, ['CCBDE', 'AAADE', 'AAABF', 'CCBBF']));
