const fs = require("fs");
const { rootCertificates } = require("tls");

inputData = fs.readFileSync("input.txt", "utf8");
inputData = inputData
  .split(/\r?\n/)
  .map((line) => line.split(" "))
  .map((line) => (line.length > 1 ? [line[0], Number(line[1])] : line));

const cyclesPerInstrucion = {
  noop: 1,
  addx: 2,
};

const printCrt = (crt) => {
  for (let row of crt) {
    console.log(row.join(""));
  }
};

const solution01 = (inputData) => {
  let x = 1;
  let cycleCounter = 0;
  const signalStrengths = [];

  //instructions loop
  for (let [instruction, v] of inputData) {
    //cycles loop
    for (let i = 0; i < cyclesPerInstrucion[instruction]; i++) {
      cycleCounter++;

      if (!((cycleCounter - 20) % 40)) {
        signalStrengths.push(cycleCounter * x);
      }

      if (signalStrengths.length === 6) {
        return signalStrengths.reduce((sum, v) => sum + v);
      }
    }

    //update x
    if (v) {
      x += v;
    }
  }

  return;
};

const solution02 = (inputData) => {
  let x = 1;
  let cycleCounter = 0;
  const crt = [];
  let crtRow = [];

  //instructions loop
  for (let [instruction, v] of inputData) {
    //cycles loop
    for (let i = 0; i < cyclesPerInstrucion[instruction]; i++) {
      cycleCounter++;

      let crtX = (cycleCounter - 1) % 40;
      const spritePosition = [x, x + 1, x - 1];
      crtRow.push(spritePosition.includes(crtX) ? "#" : " ");

      if (!(cycleCounter % 40)) {
        crt.push(crtRow);
        crtRow = [];
      }
    }

    //update x
    if (v) {
      x += v;
    }
  }

  return crt;
};

console.log(`Solution 01: ${solution01(inputData)}`);
console.log("Solution 02:");
printCrt(solution02(inputData));
