function solution(n, m, x, y, r, c, k) {
    let answer = 'impossible';
    const dx = [1, 0, 0, -1];
    const dy = [0, -1, 1, 0];
    let isDone = false

    function dfs(currentX,currentY,path) {
        if (k < path.length + Math.abs(currentX - r) + Math.abs(currentY - c)) return
        if (isDone) return
        if (path.length === k && currentX === r && currentY === c) {
            answer = path
            isDone = true
        } else if (path.length < k) {
            for (let i = 0; i < 4; i++){
                const nx = currentX + dx[i]
                const ny = currentY + dy[i]
                if (1 <= nx && nx <= n && 1 <= ny && ny <= m) {
                    if (i === 0) dfs(nx,ny,path+'d')
                    if (i === 1) dfs(nx,ny,path+'l')
                    if (i === 2) dfs(nx,ny,path+'r')
                    if (i === 3) dfs(nx,ny,path+'u')
                }
            }
        }
    }

    if ((k - (Math.abs(x - r) + Math.abs(y - c))) % 2 === 1) return "impossible"
    dfs(x,y,'')
    return answer;
}

console.log(solution(3,4,2,3,3,1,5))
console.log(solution(2,2,1,1,2,2,2))
// console.log(solution(3,3,1,2,3,3,4))
