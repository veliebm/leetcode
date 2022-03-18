var climbStairs = function (n) {
  let [a, b] = [1, 1];
  for (let _ = 0; _ < n; _++) {
    [a, b] = [b, a + b];
  }
  return a;
};
console.log(1);
