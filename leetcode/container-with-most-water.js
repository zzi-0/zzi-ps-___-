/**
 * @param {number[]} height
 * @return {number}
 */

// https://leetcode.com/problems/container-with-most-water/
var maxArea = function(list) {
    let lt = 0;
    let rt = list.length - 1;

    let answer = 0;

    while (lt < rt) {
        const width = rt - lt;
        const height = list[rt] < list[lt] ? list[rt] : list[lt];

        const amount = width * height;

        if (answer < amount) {
            answer = amount;
        }
        if (list[lt] < list[rt]) {
            lt += 1;
        } else {
            rt -= 1;
        }
    }

    return answer;
    
};
