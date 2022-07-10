// some -> 해당하는 원소가 있는지 확인할 때 유용
const array = [1, 2, 3, 4, 5];
const even = (element) => element % 2 === 0;

console.log(array.some(even));
