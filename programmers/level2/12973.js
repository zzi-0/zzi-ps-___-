function solution(s) {
    const arr = [];

    for (let i = 0; i < s.length; i++) {
        arr.push(s[i]);
        if (arr[arr.length - 1] === arr[arr.length - 2]) {
            arr.pop();
            arr.pop();
        }
    }

    return arr.join('') === '' ? 1 : 0;
}
console.log(solution('dccddd'));
