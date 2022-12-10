const fs = require("fs");
const { rootCertificates } = require("tls");

inputData = fs.readFileSync("input.txt", "utf8");
inputData = inputData
  .split(/\r?\n/)
  .map((line) => line.split(" "))
  .map((line) => [line[0], Number(line[1])]);

const solution = (inputData, length) => {
  let rope = [...new Array(length + 1)].map((v) => [0, 0]);

  const tailVisitedPositions = new Set();

  for (let [direction, steps] of inputData) {
    for (let step = 0; step < steps; step++) {
      //loop the rope
      for (let i = 0; i < rope.length; i++) {
        let dx = 0;
        let dy = 0;

        if (i === 0) {
          switch (direction) {
            case "L":
              dx = -1;
              break;
            case "R":
              dx = 1;
              break;
            case "U":
              dy = -1;
              break;
            case "D":
              dy = 1;
              break;
          }
        } else {
          diff_x = rope[i - 1][0] - rope[i][0];
          diff_y = rope[i - 1][1] - rope[i][1];

          max_diff = Math.max(Math.abs(diff_x), Math.abs(diff_y));

          if (max_diff > 1) {
            dx = Math.sign(diff_x);
            dy = Math.sign(diff_y);
          }
        }

        rope[i][0] += dx;
        rope[i][1] += dy;

        if (i === length) {
          tailVisitedPositions.add([rope[i][0], rope[i][1]].join(","));
        }
      }
    }
  }

  return tailVisitedPositions.size;
};

console.log(`Solution 01: ${solution(inputData, 1)}`);
console.log(`Solution 02: ${solution(inputData, 9)}`);
