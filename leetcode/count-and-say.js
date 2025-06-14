/**
 * @param {number} n
 * @return {string}
 */

// countAndSay(1) = "1"
// countAndSay(2) = RLE of "1" = "11"
// countAndSay(3) = RLE of "11" = "21"
// countAndSay(4) = RLE of "21" = "1211"

function recursive(current, limit, answer) {
    if (current === limit) return answer;
    const array = answer.split("");
    let ans = "";
    let cur = "";
    let count = 0;
    
    array.forEach((item, index) => {
        // 처음 아이템 
        if (cur === "") {
            cur = item;
        }
        if (item === cur) {
            count += 1;
        } else {
            ans += count;
            ans += cur;
            cur = item;
            count = 1;
        }  
        // 마지막 아이템 
        if (index === array.length - 1) {
            ans += count;
            ans += cur;
        }
    })
    
    return recursive (current+ 1, limit, ans);
    
}

function countAndSay(n){
    return recursive(1,n,"1");
};
