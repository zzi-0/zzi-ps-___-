const isPrime = (n) => {
  if (n === 2) return true;
  for (let i = 2; i <= Math.ceil(Math.sqrt(n)); i++) {
    if (n % i === 0) {
      return false;
    }
  }
  return true;
};

function solution(n) {
  let count = 0;
  for (let i = 2; i <= n; i++) {
    if (isPrime(i)) count++;
  }
  return count;
}

console.log(solution(10));
