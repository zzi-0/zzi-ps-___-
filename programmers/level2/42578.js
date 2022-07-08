function solution(clothes) {
    const clothesMap = new Map();
    let combination = 1;

    clothes.forEach((c) => {
        const [item, type] = c;
        if (clothesMap.has(type)) {
            const clothesList = clothesMap.get(type);
            clothesList.push(item);
            clothesMap.set(type, clothesList);
        } else {
            clothesMap.set(type, [item]);
        }
    });

    if (clothesMap.size === 1) return clothes.length;

    for (let [index, value] of clothesMap) {
        combination *= value.length + 1;
    }

    return combination - 1;
}

console.log(
    solution([
        ['yellow_hat', 'headgear'],
        ['blue_sunglasses', 'eyewear'],
        ['green_turban', 'headgear'],
    ])
);
