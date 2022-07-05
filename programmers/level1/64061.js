function solution(board, moves) {
    let answer = 0;
    let basket = [];

    for (const move of moves) {
        for (let i = 0; i < board.length; i++) {
            if (board[i][move - 1] !== 0) {
                basket.push(board[i][move - 1]);
                board[i][move - 1] = 0;
                break;
            }
        }
        for (let i = 0; i < basket.length - 1; i++) {
            if (basket[i] === basket[i + 1]) {
                answer += 2;
                basket.pop();
                basket.pop();
            }
        }
    }

    return answer;
}

console.log(
    solution(
        [
            [0, 0, 0, 0, 0],
            [0, 0, 1, 0, 3],
            [0, 2, 5, 0, 1],
            [4, 2, 4, 4, 2],
            [3, 5, 1, 3, 1],
        ],
        [1, 5, 3, 5, 1, 2, 1, 4]
    )
);
