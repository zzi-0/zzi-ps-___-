function solution(sticker) {
  // [14, 6, 5, 11, 3, 9, 2, 10] 솔루션 !
  // [14,6,5,11,3,9,2] dp  or [6,5,11,3,9,2,10] dp
  // 이렇게 풀었더니 효율성 애매하긴 함, 시간 초과 날 때도 있고 성공할 때도 있음
  let dp1 = Array(sticker.length + 1).fill(0);
  let dp2 = Array(sticker.length + 1).fill(0);

  if (sticker.length === 1) return sticker[0];
  if (sticker.length === 2) return Math.max(sticker[0], sticker[1]);
  if (sticker.length === 3) return Math.max(sticker[0], sticker[1], sticker[2]);

  dp1[0] = sticker[0];
  dp1[1] = Math.max(sticker[0], sticker[1]);
  dp1[2] = Math.max(dp1[0] + sticker[2], dp1[1]);
  for (let i = 3; i < sticker.length - 1; i++) {
    dp1[i] = Math.max(dp1[i - 1], dp1[i - 2] + sticker[i]);
  }

  dp1[0] = 0;
  dp2[1] = Math.max(0, sticker[1]);
  dp2[2] = Math.max(dp2[0] + sticker[2], dp2[1]);
  for (let i = 3; i < sticker.length; i++) {
    dp2[i] = Math.max(dp2[i - 1], dp2[i - 2] + sticker[i]);
  }

  const d1Max = Math.max(...dp1);
  const d2Max = Math.max(...dp2);

  return d1Max > d2Max ? d1Max : d2Max;
}

console.log(solution([1]));
console.log(solution([1, 2]));
console.log(solution([1, 2, 3]));
console.log(solution([1, 3, 2, 5, 4]));
// [14,6,5,11,3,9,2] dp  or [6,5,11,3,9,2,10] dp
// 14 + 20 = 34 or   36
console.log(solution([14, 6, 5, 11, 3, 9, 2, 10]));
