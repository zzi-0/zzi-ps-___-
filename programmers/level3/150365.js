function solution(n, m, x, y, r, c, k) {
    let answer = '';
    const dx = [1, 0, 0, -1];
    const dy = [0, -1, 1, 0];

    const queue = [];
    queue.push([x-1,y-1,''])

    function bfs() {
        while(queue.length) {
            const [currentX,currentY,path] = queue.pop();
            if (path.length === k && currentX === r-1 && currentY === c-1) {
                answer = path;
                break;
            }
            if (path.length < k) {
                for (let i = 0; i< 4; i++){
                    const nx = currentX + dx[i]
                    const ny = currentY + dy[i]
                    if (0 <= nx && nx < n && 0 <= ny && ny < m){
                        if (i === 0) queue.unshift([nx,ny,path+'d'])
                        if (i === 1) queue.unshift([nx,ny,path+'l'])
                        if (i === 2) queue.unshift([nx,ny,path+'r'])
                        if (i === 3) queue.unshift([nx,ny,path+'u'])
                    }
                }
            }
        }
    }

    bfs()
    return answer || 'impossible';
}

console.log(solution(2,2,1,1,2,2,2))
