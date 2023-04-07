const fs = require("fs");

inputData = fs.readFileSync("input.txt", "utf8");

inputData = inputData
  .split(/\r?\n/)
  .map((v) => v.trim())
  .map((v) => v.split(","))
  .flat()
  .map((v) => Number(v));

console.log(inputData);

const logArr = (arr) => {
  for ([i, v] of arr.entries()) {
    console.log(i, v);
  }
};

const createArrWithZeroes = (length) => [...Array(length)].map((v) => 0);

const solution = (positions, increaseFuel = false) => {
  const minPos = Math.min(...positions);
  const maxPos = Math.max(...positions);

  console.log(minPos);
  console.log(maxPos);

  //test different align values

  let lowestSum = Infinity,
    lowestAlignPos = 0;
  let counter = 0;
  for (let testPos = minPos; testPos <= maxPos; testPos++) {
    let sum = 0;

    for (pos of positions) {
      counter++;

      const stepsDiff = Math.abs(pos - testPos);

      if (!increaseFuel) {
        sum += stepsDiff;
      } else {
        for (let i = 0; i < stepsDiff; i++) {
          sum += i + 1;
        }
      }

      //break if sum is already higher than current lowest
      if (sum > lowestSum) break;
    }

    if (sum < lowestSum) {
      lowestSum = sum;
      lowestAlignPos = testPos;
    }

    console.log(testPos, sum);
  }

  console.log("counter", counter);
  return lowestSum;
};

console.log(`Solution 01: ${solution(inputData)}`);
console.log(`Solution 02: ${solution(inputData, true)}`);
