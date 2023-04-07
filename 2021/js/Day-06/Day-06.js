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

const solution = (initState, days) => {
  const maxTimer = 8;

  //create empty array. index = timer. value = number of fish with that timer
  let statesOfFish = createArrWithZeroes(maxTimer + 1);

  for (fish of initState) {
    statesOfFish[fish] += 1;
  }

  for (let day = 0; day < days; day++) {
    //rotate array
    statesOfFish.push(statesOfFish.shift());

    //add new fish
    statesOfFish[6] = statesOfFish[6] + statesOfFish[8];

    console.log(statesOfFish.reduce((sum, v) => sum + v));
  }

  return statesOfFish.reduce((sum, v) => sum + v);
};

console.log(`Solution 01: ${solution([...inputData], 80)}`);
console.log(`Solution 02: ${solution([...inputData], 256)}`);
