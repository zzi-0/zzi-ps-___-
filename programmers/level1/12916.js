function solution(s) {
  let pCount = 0;
  let yCount = 0;

  for (const alphabet of s.toUpperCase()) {
    if (alphabet === "P") pCount++;
    if (alphabet === "Y") yCount++;
  }
  return pCount === yCount;
}

console.log(solution("pPoooyY"));
