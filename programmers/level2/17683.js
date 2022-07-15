function solution(m, musicinfos) {
    let matchingMusic = [];
    for (let i = 0; i < musicinfos.length; i++) {
        let [startTime, endTime, title, melody] = musicinfos[i].split(',');

        melody = melody
            .replace(/(A#)/g, 'a')
            .replace(/(C#)/g, 'c')
            .replace(/(D#)/g, 'd')
            .replace(/(F#)/g, 'f')
            .replace(/(G#)/g, 'g');

        startTime = new Date('2022', '07', '15', startTime.split(':')[0], startTime.split(':')[1]);
        endTime = new Date('2022', '07', '15', endTime.split(':')[0], endTime.split(':')[1]);
        const elapsedMSec = endTime.getTime() - startTime.getTime();
        const elapsedMin = elapsedMSec / 1000 / 60;
        const quotient = Math.ceil(elapsedMin / melody.length);
        melody = melody.repeat(quotient);

        melody = melody.substr(0, elapsedMin);

        m = m
            .replace(/(A#)/g, 'a')
            .replace(/(C#)/g, 'c')
            .replace(/(D#)/g, 'd')
            .replace(/(F#)/g, 'f')
            .replace(/(G#)/g, 'g');

        if (melody.includes(m)) matchingMusic.push([i, title, elapsedMin]);
    }
    matchingMusic.sort((a, b) => b[2] - a[2]);
    if (matchingMusic.length === 0) return '(None)';
    return matchingMusic[0][1];
}

console.log(solution('ABC#', ['12:00,12:14,HELLO,ABC#AG', '13:00,13:14,WORLD,C#DEFAB']));
