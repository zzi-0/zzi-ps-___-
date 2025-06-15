/**
 * @param {character[][]} grid
 * @return {number}
 */
function numIslands(grid) {
    
    const n = grid.length;
    const m = grid[0].length;
    const dx = [0, 1, 0, -1];
    const dy = [1, 0, -1, 0];
    
    
    let answer = 0;
    
    function dfs(x,y) {
     
        for (let i = 0; i< 4; i++) {
            const nx = dx[i] + x;
            const ny = dy[i] + y;

            if (nx >= 0 && ny >= 0 && nx < n && ny < m) {
                if (grid[nx][ny] == 1) {
                    grid[nx][ny] = 0;   
                    dfs(nx,ny);
                }
            }

        }   
    }
    
    for (let i = 0; i < n; i++) {
        for (let j = 0; j < m; j++) {
            if (grid[i][j] == 1) {
                dfs(i,j);
                answer += 1;
            }
        }
    }
    
    
    
    return answer;
    
};
