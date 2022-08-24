function solution(board) {
    let answer = 0;

    if (board.length === 1 && board[0].length === 1) return 1;

    for (let i = 1; i < board.length; i++) {
        for (let j = 1; j < board[i].length; j++) {
            if (board[i][j]) {
                const left = board[i - 1][j];
                const right = board[i][j - 1];
                const cross = board[i - 1][j - 1];
                const min = Math.min(left, right, cross);
                board[i][j] = min + 1;
                answer = Math.max(board[i][j], answer);
            }
        }
    }

    return answer * answer;
}

console.log(
    solution([
        [0, 1, 1, 1],
        [1, 1, 1, 1],
        [1, 1, 1, 1],
        [0, 0, 1, 0],
    ])
);
