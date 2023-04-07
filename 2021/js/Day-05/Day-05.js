const fs = require("fs");

inputData = fs.readFileSync("input.txt", "utf8");

inputData = inputData.split(/\r?\n/).map((v) => v.trim());

inputData = inputData.map((v) =>
  v
    .split(" -> ")
    .map((v) => v.split(","))
    .map((v) => v.map((v) => Number(v)))
);

console.log(inputData);

const solution = (lines, ignoreDiagonals = true) => {
  drawnLines = [];

  for (line of lines) {
    const [x1, y1, x2, y2] = line.flat();

    let dirX = x1 < x2 ? 1 : x1 > x2 ? -1 : 0;
    let dirY = y1 < y2 ? 1 : y1 > y2 ? -1 : 0;

    if (dirX && dirY && ignoreDiagonals) {
      continue;
    }

    //wonder if this will work:
    let distance = Math.abs(x1 - x2) || Math.abs(y1 - y2);

    for (let i = 0; i < distance + 1; i++) {
      x = x1 + dirX * i;
      y = y1 + dirY * i;

      drawnLines[[x, y]] = (drawnLines[[x, y]] || 0) + 1;
    }
  }
  // console.log(drawnLines);

  let counter = 0;

  console.log(counter);

  for (k in drawnLines) {
    if (drawnLines[k] > 1) counter++;
  }

  return counter;
};

console.log(`Solution 01: ${solution(inputData)}`);
console.log(`Solution 02: ${solution(inputData, false)}`);
