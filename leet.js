var climbStairs = function (n) {
  let [a, b] = [1, 1];
  for (_ = 0; _ < n; _++) {
    [a, b] = [a, a + b];
  }
  return a;
};
console.log(1)