function solution(board) {
  let answer = -1;
  const dx = [-1, 0, 1, 0];
  const dy = [0, 1, 0, -1];
  const n = board.length;
  const m = board[0].length;
  let r_i = 0;
  let r_j = 0;
  let g_i = 0;
  let g_j = 0;
  const visited = Array.from(Array(n), () => Array(m).fill(0));
  const queue = [];

  for (let i = 0; i < n; i++) {
    for (let j = 0; j < m; j++) {
      if (board[i][j] === "R") {
        r_i = i;
        r_j = j;
      }
      if (board[i][j] === "G") {
        g_i = i;
        g_j = j;
      }
    }
  }

  queue.push([r_i, r_j, 0]);

  while (queue.length) {
    let [x, y, count] = queue.shift();
    //console.log(x, y, count);
    if (x === g_i && y === g_j) {
      answer = count;
      break;
    }
    const i_x = x;
    const i_y = y;
    for (let i = 0; i < 4; i++) {
      x = i_x;
      y = i_y;
      while (1) {
        nx = dx[i] + x;
        ny = dy[i] + y;
        if (0 <= nx && nx < n && 0 <= ny && ny < m && board[nx][ny] !== "D") {
          x = nx;
          y = ny;
        } else {
          break;
        }
      }
      //  console.log("i", i, "i_x", i_x, "i_y", i_y, "x", x, "y", y);
      if ((x !== i_x || y !== i_y) && visited[x][y] === 0) {
        queue.push([x, y, count + 1]);
        visited[x][y] = 1;
      }
    }
  }

  return answer;
}

console.log(solution(["...D..R", ".D.G...", "....D.D", "D....D.", "..D...."]));
console.log(solution([".D.R", "....", ".G..", "...D"]));
