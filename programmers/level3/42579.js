function solution(genres, plays) {
    var answer = [];
    const genreMap = new Map();
    const playArray = [];
    for (let i = 0; i < genres.length; i++) {
        if (genreMap.has(genres[i])) {
            const playCount = genreMap.get(genres[i]);
            genreMap.set(genres[i], playCount + plays[i]);
        } else {
            genreMap.set(genres[i], plays[i]);
        }
        playArray.push([plays[i], genres[i]]);
    }
    const genreArray = [...genreMap];
    genreArray.sort((a, b) => b[1] - a[1]);
    playArray.sort((a, b) => a[0] - b[0]).reverse();

    for (const [genre, count] of genreArray) {
        let count = 0;
        for (const [playCount, playGenre] of playArray) {
            console.log(playCount, playGenre);
            if (playGenre === genre && count < 2) {
                answer.push(plays.indexOf(playCount));
                delete plays[plays.indexOf(playCount)];
                count++;
            }
        }
    }

    return answer;
}

console.log(solution(['classic', 'pop', 'classic', 'classic', 'pop'], [500, 600, 150, 800, 2500]));
