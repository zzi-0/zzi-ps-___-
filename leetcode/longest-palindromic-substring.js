/**
 * @param {string} s
 * @return {string}
 */

function isPalindrome(s, left, right) {
    while(left > 0 && right < s.length) {
        if (s[left] === s[right]) {
            left -= 1;
            right += 1;   
        } else {
            break;
        }
    }
    if (s[left] === s[right]) {
        return s.slice(left, right + 1);
    }
    else {
        return s.slice(left + 1, right);   
    }
}

function longestPalindrome(s) {
   if (s.length < 2) return s;
   let result = '';
    
   for (let i = 0; i < s.length; i++) {
       // 홀수 길이
       const odd = isPalindrome(s, i, i);
       if (odd.length > result.length) {
           result = odd;
       }
       
       // 짝수 길이
       const even = isPalindrome(s, i, i+1);
       if (even.length > result.length) {
           result = even;
       }
       
   }
    
    return result;
    
};
