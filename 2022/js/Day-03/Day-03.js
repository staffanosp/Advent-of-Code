const fs = require("fs");

inputData = fs.readFileSync("input.txt", "utf8");
inputData = inputData.split(/\r?\n/).map((line) => line.split(""));

function getCommonItem(array) {
  outer: for (let item of array[0]) {
    for (let i = 1; i < array.length; i++) {
      if (array[i].includes(item)) {
        continue;
      } else {
        continue outer;
      }
    }
    return item;
  }
}

function convertToPriority(items) {
  const scores = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ";
  return items.map((item) => scores.indexOf(item) + 1);
}

const Solution01 = (inputData) => {
  const rucksacks = inputData.map((line) => [
    line.slice(0, line.length / 2),
    line.slice(line.length / 2),
  ]);

  return convertToPriority(
    rucksacks.map((rucksack) => getCommonItem(rucksack))
  ).reduce((sum, v) => sum + v);
};

const Solution02 = (inputData) => {
  const rucksacksInGroupOf3 = [];
  for (let i = 0; i < inputData.length; i += 3) {
    rucksacksInGroupOf3.push(inputData.slice(i, i + 3));
  }

  return convertToPriority(
    rucksacksInGroupOf3.map((rucksacks) => getCommonItem(rucksacks))
  ).reduce((sum, v) => sum + v);
};

console.log(`Solution 01: ${Solution01(inputData)}`);
console.log(`Solution 02: ${Solution02(inputData)}`);
