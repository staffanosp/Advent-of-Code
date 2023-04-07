const fs = require("fs");

inputData = fs.readFileSync("input.txt", "utf8");

inputData = inputData.split(/\r?\n/);

// console.log(inputData);

const Solution01 = (inputData) => {
  const binaryLength = inputData[0].length;
  const reportLength = inputData.length;
  let [gamma, epsilon] = ["", ""];

  for (let pos = 0; pos < binaryLength; pos++) {
    let [ones, zeroes] = [0, 0];

    for (let line = 0; line < reportLength; line++) {
      if (inputData[line][pos] === "0") {
        zeroes += 1;
      } else {
        ones += 1;
      }
    }
    if (zeroes > ones) {
      gamma += 0;
      epsilon += 1;
    } else {
      gamma += 1;
      epsilon += 0;
    }
  }

  return parseInt(gamma, 2) * parseInt(epsilon, 2);
};

const Solution02 = (inputData) => {
  oxygen = [...inputData];
  co2 = [...inputData];
  const binaryLength = inputData[0].length;
  // const reportLength = inputData.length;
  // let [gamma, epsilon] = ["", ""];

  //find oxygen rating
  let pos = 0;
  while (oxygen.length > 1) {
    // for (let pos = 0; pos < binaryLength; pos++) {
    let [ones, zeroes] = [0, 0];

    //find most common
    for (let line = 0; line < oxygen.length; line++) {
      if (oxygen[line][pos] === "0") {
        zeroes += 1;
      } else {
        ones += 1;
      }
    }

    //keep only lines where most common bit is in current pos
    oxygen = oxygen.filter(
      (binary) => binary[pos] === (zeroes > ones ? "0" : "1")
    );

    // console.log(pos, zeroes, ones, oxygen);
    pos++;
  }

  //find co2 rating
  pos = 0;
  while (co2.length > 1) {
    // for (let pos = 0; pos < binaryLength; pos++) {
    let [ones, zeroes] = [0, 0];

    //find most common
    for (let line = 0; line < co2.length; line++) {
      if (co2[line][pos] === "0") {
        zeroes += 1;
      } else {
        ones += 1;
      }
    }

    //keep only lines where least common bit is in current pos
    co2 = co2.filter((binary) => binary[pos] === (zeroes > ones ? "1" : "0"));
    // console.log(pos, zeroes, ones, co2);
    pos++;
  }

  return parseInt(oxygen[0], 2) * parseInt(co2[0], 2);
};

console.log(`Solution 01: ${Solution01(inputData)}`);
console.log(`Solution 02: ${Solution02(inputData)}`);
