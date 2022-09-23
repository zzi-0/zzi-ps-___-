function solution(board) {
    let answer = 0;
    let dx = [-1, -1, 0, 1, 1, 1, 0, -1];
    let dy = [0, 1, 1, 1, 0, -1, -1, -1];

    function dfs(x, y) {
        for (let i = 0; i < 8; i++) {
            let nx = x + dx[i];
            let ny = y + dy[i];
            if (nx >= 0 && nx < board.length && ny >= 0 && ny < board.length) {
                if (board[nx][ny]) {
                    board[nx][ny] = 0;
                    dfs(nx, ny);
                }
            }
        }
    }

    for (let i = 0; i < board.length; i++) {
        for (let j = 0; j < board.length; j++) {
            if (board[i][j]) {
                board[i][j] = 0;
                dfs(i, j);
                answer++;
            }
        }
    }
    return answer;
}

let arr = [
    [1, 1, 0, 0, 0, 1, 0],
    [0, 1, 1, 0, 1, 1, 0],
    [0, 1, 0, 0, 0, 0, 0],
    [0, 0, 0, 1, 0, 1, 1],
    [1, 1, 0, 1, 1, 0, 0],
    [1, 0, 0, 0, 1, 0, 0],
    [1, 0, 1, 0, 1, 0, 0],
];

console.log(solution(arr));
