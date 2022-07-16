//9:15
function solution(n, t, m, p) {
    var answer = '';
    let before = '';
    let game = '';
    let i = 0;
    const b = true;

    while (b) {
        before = game;
        game += i.toString(n).toUpperCase();
        i++;
        for (let j = before.length; j < game.length; j++) {
            if (answer.length === t) return answer;
            if ((j + 1) % m === p % m) answer += game[j];
        }
    }
}

// 0 1 1
console.log(solution(16, 16, 2, 1));
