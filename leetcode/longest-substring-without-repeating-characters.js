/**
 * @param {string} s
 * @return {number}
 */
function lengthOfLongestSubstring(s) {
    let answer = 1;
    if (s.length < 2) {
        return s.length;
    }
    
    for (let i = 0; i < s.length; i++) {
        for (let j = i; j < s.length; j++) {
            if (s.slice(i, j).includes(s[j])) {
                if (j - i > answer) {
                    answer = j - i;
                }
                break;
            } else {
                if (j - i + 1 > answer) {
                    answer = j - i + 1;
                }
            }
            
        }
    }
    
    return answer;
    
};
