/**
 * @param {string[]} strs
 * @return {string[][]}
 */

function isAnagram(s, t) {
  if (s.length !== t.length) return false;
  const count = Array(26).fill(0);
  for (let i = 0; i < s.length; i++) {
    count[s.charCodeAt(i) - 97]++; 
    count[t.charCodeAt(i) - 97]--;
  }

  return count.every((n) => n === 0);
}

function groupAnagrams(strs) {
    const answer = [];
    const check = Array.from({length : strs.length},() => 0);
    
    for (let i = 0; i < strs.length; i++) {
       const temp = [];
        if (check[i]) {
            continue;
        }
        for (let j = i; j <strs.length; j++) {
            if (isAnagram(strs[i],strs[j])) {
                check[j] = 1;
                temp.push(strs[j])
            }
        }
        answer.push(temp);
    }
    
    return answer;
    
};
