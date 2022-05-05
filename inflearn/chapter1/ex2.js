const solution = (firstLen, secondLen, thirdLen) => {
  let longestLen = firstLen;
  let shortSumLen = secondLen + thirdLen;

  if (secondLen > thirdLen && secondLen > firstLen) {
    longestLen = secondLen;
    shortSumLen = firstLen + thirdLen;
  }

  if (thirdLen > secondLen && thirdLen > firstLen) {
    longestLen = thirdLen;
    shortSumLen = secondLen + firstLen;
  }

  return longestLen < shortSumLen ? "YES" : "NO";
};

console.log(solution(23, 42, 7));
