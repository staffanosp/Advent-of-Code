const fs = require("fs");
const { rootCertificates } = require("tls");

inputData = fs.readFileSync("input.txt", "utf8");
inputData = inputData
  .split(/\r?\n/)
  .map((line) => line.split(" "))
  .map((line) => [line[0], Number(line[1])]);

const clamp = (v, min, max) => Math.max(Math.min(v, max), min);

const solution = (inputData, length) => {
  let head_pos = [0, 0];
  let tail = [...new Array(length)].map((v) => [0, 0]);

  const tailVisitedPositions = new Set();

  for (let [direction, steps] of inputData) {
    let head_dx = 0;
    let head_dy = 0;

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
      head_pos[0] += head_dx;
      head_pos[1] += head_dy;

      //loop the tail
      for (let [i, knot] of tail.entries()) {
        let target_pos;
        if (i === 0) {
          target_pos = head_pos;
        } else {
          target_pos = tail[i - 1];
        }

        diff_x = target_pos[0] - knot[0];
        diff_y = target_pos[1] - knot[1];

        max_diff = Math.max(Math.abs(diff_x), Math.abs(diff_y));

        let tail_dx = 0;
        let tail_dy = 0;

        if (max_diff > 1) {
          tail_dx = clamp(diff_x, -1, 1);
          tail_dy = clamp(diff_y, -1, 1);
        }

        knot[0] += tail_dx;
        knot[1] += tail_dy;

        if (i === length - 1) {
          tailVisitedPositions.add([knot[0], knot[1]].join(","));
        }
      }
    }
  }

  return tailVisitedPositions.size;
};

console.log(`Solution 01: ${solution(inputData, 1)}`);
console.log(`Solution 02: ${solution(inputData, 9)}`);
