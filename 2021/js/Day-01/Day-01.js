const fs = require("fs");

inputData = fs.readFileSync("input.txt", "utf8");
inputData = inputData.split(/\r?\n/).map((v) => Number(v));

const Solution01 = (inputData) => {
  let counter = 0;

  for (let i = 0; i < inputData.length; i++) {
    if (i === 0) continue;
    if (inputData[i] > inputData[i - 1]) counter += 1;
  }

  return counter;
};

const Solution02 = (inputData) => {
  let counter = 0;
  let windowSums = [];

  //Create an array with the sum of the moving windows
  for (let i = 0; i < inputData.length - 2; i++) {
    const windowSum = inputData.slice(i, i + 3).reduce((sum, v) => sum + v);
    windowSums.push(windowSum);
  }

  //check how many times the moving windows increase
  for (let i = 0; i < windowSums.length; i++) {
    if (i === 0) continue;
    if (windowSums[i] > windowSums[i - 1]) counter += 1;
  }

  return counter;
};

console.log(`Solution 01: ${Solution01(inputData)}`);
console.log(`Solution 02: ${Solution02(inputData)}`);
