/*
- 삼각형 판별하기
길이가 서로 다른 A, B, C 세 개의 막대 길이가 주어지면 이 세 막대로 삼각형을 만들 수 있 으면 “YES"를 출력하고, 만들 수 없으면 ”NO"를 출력한다.

▣ 입력설명
첫 번째 줄에 100이하의 서로 다른 A, B, C 막대의 길이가 주어진다.

▣ 출력설명
첫 번째 줄에 “YES", "NO"를 출력한다.

*/

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
