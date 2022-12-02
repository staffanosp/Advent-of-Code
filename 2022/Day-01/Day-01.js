const fs = require("fs");

inputData = fs.readFileSync("input.txt", "utf8");
inputData = inputData.split(/\r?\n/);
//add an extra empty item cause that what marks "next elf"
inputData.push("");

let elvesCalories = [];

let caloriesToAdd = [];
for (data of inputData) {
  if (data) {
    caloriesToAdd.push(Number(data));
  } else {
    elvesCalories.push(caloriesToAdd.reduce((sum, v) => sum + v));
    caloriesToAdd = [];
  }
}

const Solution01 = (elvesCalories) => {
  return Math.max(...elvesCalories);
};

const Solution02 = (elvesCalories) => {
  elvesCalories = [...elvesCalories];
  elvesCalories = elvesCalories.sort((a, b) => b - a);
  elvesCalories.splice(3);

  return elvesCalories.reduce((sum, v) => sum + v);
};

console.log(`Solution 01: ${Solution01(elvesCalories)}`);
console.log(`Solution 02: ${Solution02(elvesCalories)}`);
