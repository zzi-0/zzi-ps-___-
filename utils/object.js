// 반복문으로 객체 만드는 법 -> 객체에 담아서 써야할 때 유용 (만약에 index와 priority가 둘다 있어야할 때)
const priorities = [2, 1, 3, 2];
var arr = priorities.map((priority, index) => {
    return {
        index: index,
        priority: priority,
    };
});

console.log(arr);
