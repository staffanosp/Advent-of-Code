const fs = require("fs");

inputData = fs.readFileSync("input.txt", "utf8");

inputData = inputData
  .split(/\r?\n/)
  .map((v) => v.split(" "))
  .map((v) => [v[0], Number(v[1])]);

const Solution01 = (inputData) => {
  let horizontal = 0,
    depth = 0;

  inputData.forEach((el) => {
    let [instruction, v] = el;

    switch (instruction) {
      case "forward":
        horizontal += v;
        break;
      case "up":
        depth -= v;
        break;
      case "down":
        depth += v;
        break;
    }
  });

  return depth * horizontal;
};

const Solution02 = (inputData) => {
  let horizontal = 0,
    depth = 0,
    aim = 0;

  inputData.forEach((el) => {
    let [instruction, v] = el;

    switch (instruction) {
      case "forward":
        horizontal += v;
        depth += aim * v;
        break;
      case "up":
        aim -= v;
        break;
      case "down":
        aim += v;
        break;
    }
  });

  return depth * horizontal;
};

console.log(`Solution 01: ${Solution01(inputData)}`);
console.log(`Solution 02: ${Solution02(inputData)}`);
