function solution(files) {
    let fileList = [];
    for (let i = 0; i < files.length; i++) {
        let head = '';
        let number = '';
        for (const char of files[i]) {
            if (char !== ' ' && number.length !== 0 && isNaN(char)) break;
            if (char === ' ' || (isNaN(char) && number.length === 0)) head += char;
            else if (!isNaN(char)) number += char;
        }
        fileList.push({ file: files[i], head: head.toUpperCase(), number: number });
    }
    fileList.sort((a, b) => {
        if (a.head < b.head) return -1;
        else if (a.head > b.head) return 1;
        else return a.number - b.number;
    });

    return fileList.map((file) => file.file);
}

console.log(solution(['muzi1.png4', 'MUZI1.png3', 'MUZI1.png2', 'muzi1.png1']));
