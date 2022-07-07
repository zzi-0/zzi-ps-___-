function solution(s) {
  for (const alpha of s) {
    if (isNaN(alpha)) return false;
  }
  if (s.length === 4 || s.length === 6) return true;
  else return false;
}

console.log(solution("12364"));
