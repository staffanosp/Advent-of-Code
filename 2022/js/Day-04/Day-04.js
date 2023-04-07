const fs = require("fs");

inputData = fs.readFileSync("input.txt", "utf8");
inputData = inputData
  .split(/\r?\n/)
  .map((line) =>
    line
      .split(",")
      .map((pair) => pair.split("-").map((number) => Number(number)))
  );

const Solution01 = (inputData) => {
  let counter = 0;
  for (pair of inputData) {
    if (
      (pair[0][0] >= pair[1][0] && pair[0][1] <= pair[1][1]) ||
      (pair[1][0] >= pair[0][0] && pair[1][1] <= pair[0][1])
    ) {
      counter++;
    }
  }
  return counter;
};

const Solution02 = (inputData) => {
  let counter = 0;
  for (pair of inputData) {
    if (
      (pair[0][0] >= pair[1][0] && pair[0][0] <= pair[1][1]) ||
      (pair[0][1] >= pair[1][0] && pair[0][1] <= pair[1][1]) ||
      (pair[1][0] >= pair[0][0] && pair[1][0] <= pair[0][1]) ||
      (pair[1][1] >= pair[0][0] && pair[1][1] <= pair[0][1])
    ) {
      counter++;
    }
  }
  return counter;
};

console.log(`Solution 01: ${Solution01(inputData)}`);
console.log(`Solution 02: ${Solution02(inputData)}`);
