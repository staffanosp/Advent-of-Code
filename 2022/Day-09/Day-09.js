const fs = require("fs");

inputData = fs.readFileSync("input.txt", "utf8");
inputData = inputData
  .split(/\r?\n/)
  .map((line) => line.split(" "))
  .map((line) => [line[0], Number(line[1])]);

const clamp = (v, min, max) => Math.max(Math.min(v, max), min);

const solution01 = (inputData) => {
  let head_x = 0;
  let head_y = 0;
  let tail_x = 0;
  let tail_y = 0;
  const tailVisitedPositions = new Set();

  for (let [direction, steps] of inputData) {
    let head_dx = 0;
    let head_dy = 0;
    let tail_dx = 0;
    let tail_dy = 0;

    switch (direction) {
      case "L":
        head_dx = -1;
        break;
      case "R":
        head_dx = 1;
        break;
      case "U":
        head_dy = -1;
        break;
      case "D":
        head_dy = 1;
        break;
    }

    for (let step = 0; step < steps; step++) {
      head_x += head_dx;
      head_y += head_dy;

      diff_x = head_x - tail_x;
      diff_y = head_y - tail_y;

      max_diff = Math.max(Math.abs(diff_x), Math.abs(diff_y));

      let tail_dx = 0;
      let tail_dy = 0;

      if (max_diff > 1) {
        tail_dx = clamp(diff_x, -1, 1);
        tail_dy = clamp(diff_y, -1, 1);
      }

      tail_x += tail_dx;
      tail_y += tail_dy;

      tailVisitedPositions.add([tail_x, tail_y].join(","));
    }
  }

  return tailVisitedPositions.size;
};

console.log(`Solution 01: ${solution01(inputData)}`);
// console.log(`Solution 02: ${solution(inputData, 2)}`);
