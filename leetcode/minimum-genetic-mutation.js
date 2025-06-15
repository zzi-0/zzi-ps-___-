/**
 * @param {string} startGene
 * @param {string} endGene
 * @param {string[]} bank
 * @return {number}
 */

function getItems(bank, item,visited) {
    const items = [];
    bank.forEach((b) => {
        let diffCount = 0;
        for (let i = 0; i < b.length; i++) {
            if (b[i] !== item[i]) {
                diffCount += 1;
            }
            if (diffCount >= 2) continue;
            if (i === item.length - 1) {
                items.push(b);
            }
        }
    })

    return items;

}
function minMutation(startGene, endGene, bank) {

    const queue = [];
    let answer = 0;
    let isStop = false;
    const visited = Array(bank.length).fill(false);

    function bfs() {
        while(queue.length) {
            const [item, count] = queue.shift();
            if (item === endGene) {
                answer = count;
                isStop = true;
                break;
            } else {
                const items = getItems(bank,item);
                items.forEach((item) => {
                    const index = bank.findIndex(b => b === item)
                    if (visited[index] == false) {
                        queue.push([item, count + 1]);
                        visited[index] = true;
                    }
                })

            }
        }
    }

    queue.push([startGene, 0]);
    bfs();
    return !isStop ? -1 : answer;
    
};
