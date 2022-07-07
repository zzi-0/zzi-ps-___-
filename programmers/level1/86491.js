function solution(sizes) {
    let anotherSizeList = [];
    let maxSize = Math.max(...sizes.flat());

    for (const size of sizes) {
        if (size[0] !== maxSize && size[1] !== maxSize) {
            if (size[0] > size[1]) anotherSizeList.push(size[1]);
            else anotherSizeList.push(size[0]);
        } else if (size[0] === maxSize) anotherSizeList.push(size[1]);
        else if (size[1] === maxSize) anotherSizeList.push(size[0]);
    }

    return maxSize * Math.max(...anotherSizeList);
}

console.log(
    solution([
        [10, 7],
        [12, 3],
        [8, 15],
        [14, 7],
        [5, 15],
    ])
);
