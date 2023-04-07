const { sign } = require("crypto");
const fs = require("fs");

inputData = fs.readFileSync("input.txt", "utf8");

inputData = inputData
  .split(/\r?\n/)
  .map((v) => v.trim())
  .map((v) => v.split(""))
  .map((row) => row.map((v) => Number(v)));

// console.log(inputData);

const isLowpoint = (x, y, data) => {
  //check left
  if (x > 0) {
    if (data[y][x] >= data[y][x - 1]) return false;
  }
  //check right
  if (x < data[0].length) {
    if (data[y][x] >= data[y][x + 1]) return false;
  }

  //check top
  if (y > 0) {
    if (data[y][x] >= data[y - 1][x]) return false;
  }

  //check bottom
  if (y < data.length - 1) {
    if (data[y][x] >= data[y + 1][x]) return false;
  }

  return true;
};

const solution1 = (inputData) => {
  let riskLevels = [];

  for (let y = 0; y < inputData.length; y++) {
    for (let x = 0; x < inputData[0].length; x++) {
      if (isLowpoint(x, y, inputData)) {
        riskLevels.push(inputData[y][x] + 1);
      }
    }
  }
  console.log(riskLevels);
  return riskLevels.reduce((sum, v) => sum + v, 0);
};

console.log(`Solution 01: ${solution1(inputData)}`);
// console.log(`Solution 02: ${solution2(inputData)}`);
