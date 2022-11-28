const solution = (n, s, a, b, fares) => {
  let answer = Infinity;
  let graph = Array.from(Array(n), () => Array(n).fill(Infinity));

  for (let i = 0; i < fares.length; i++) {
    const [start, end, cost] = fares[i];
    graph[start - 1][end - 1] = cost;
    graph[end - 1][start - 1] = cost;
  }

  for (let i = 0; i < n; i++) {
    graph[i][i] = 0;
  }

  for (let k = 0; k < n; k++) {
    for (let i = 0; i < n; i++) {
      for (let j = 0; j < n; j++) {
        graph[i][j] = Math.min(graph[i][j], graph[i][k] + graph[k][j]);
      }
    }
  }

  for (let i = 0; i < n; i++) {
    answer = Math.min(
      answer,
      graph[s - 1][i] + graph[i][a - 1] + graph[i][b - 1]
    );
  }

  return answer;
};

console.log(
  solution(6, 4, 5, 6, [
    [2, 6, 6],
    [6, 3, 7],
    [4, 6, 7],
    [6, 5, 11],
    [2, 5, 12],
    [5, 3, 20],
    [2, 4, 8],
    [4, 3, 9],
  ])
);
