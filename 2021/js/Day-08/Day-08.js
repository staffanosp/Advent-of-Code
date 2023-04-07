const fs = require("fs");

inputData = fs.readFileSync("input.txt", "utf8");

inputData = inputData
  .split(/\r?\n/)
  .map((v) => v.trim())
  .map((v) => v.split(" | "))
  .map((v) => v.map((v) => v.split(" ")))
  .map((v) => Object({ signal: v[0], output: v[1] }));

// console.log(inputData);

const solution1 = (inputData) => {
  const uniqueNumbers = [2, 3, 4, 7];
  let uniqueCounter = 0;

  for (entry of inputData) {
    for (output of entry["output"]) {
      if (uniqueNumbers.includes(output.length)) uniqueCounter++;
    }
  }

  return uniqueCounter;
};

const solution2 = (inputData) => {
  const segmentsToNumbers = {
    abcefg: "0",
    cf: "1",
    acdeg: "2",
    acdfg: "3",
    bcdf: "4",
    abdfg: "5",
    abdefg: "6",
    acf: "7",
    abcdefg: "8",
    abcdfg: "9",
  };

  let allOutputs = [];

  //loop through the entries

  for (entry of inputData) {
    //sort signals by segment count
    let signalsBySegmentCount = {};

    for (i = 2; i < 8; i++) {
      signalsBySegmentCount[i] = [];
    }

    for (signal of entry["signal"]) {
      signalsBySegmentCount[signal.length].push(signal);
    }

    //find out the mapping

    let signalMap = {};

    // #1 (2 segments) are potential C F
    const C_F = signalsBySegmentCount[2][0];

    //the diff between #1 (2 segments) and #4 (4 segments) is potential B D
    let B_D = "";
    for (char of signalsBySegmentCount[4][0]) {
      if (!signalsBySegmentCount[2][0].includes(char)) {
        B_D += char;
      }
    }

    //the diff between #8 (8 segments) and (#4 (4 segments) + #7 (3 segments)) is potential E G
    let E_G = "";
    for (char of signalsBySegmentCount[7][0]) {
      if (
        !new Set([
          ...signalsBySegmentCount[4][0],
          ...signalsBySegmentCount[3][0],
        ]).has(char)
      ) {
        E_G += char;
      }
    }

    //the diff between #1 (2 segments) and #7 (3 segments) is segment A
    for (char of signalsBySegmentCount[3][0]) {
      if (!signalsBySegmentCount[2][0].includes(char)) {
        signalMap[char] = "a";
      }
    }

    //The char in B_D that is in 0,6 and 9 (segment count 6) is B, the other one is D
    if (signalsBySegmentCount[6].every((signal) => signal.includes(B_D[0]))) {
      signalMap[B_D[0]] = "b";
      signalMap[B_D[1]] = "d";
    } else {
      signalMap[B_D[0]] = "d";
      signalMap[B_D[1]] = "b";
    }

    // The char in C_F that is in 0,6 and 9 (segment count 6) is F, the other one is C
    if (signalsBySegmentCount[6].every((signal) => signal.includes(C_F[0]))) {
      signalMap[C_F[0]] = "f";
      signalMap[C_F[1]] = "c";
    } else {
      signalMap[C_F[0]] = "c";
      signalMap[C_F[1]] = "f";
    }

    // The char in E_G that is in 2,3 and 5 (segment count 5) is G, the other one is E
    if (signalsBySegmentCount[5].every((signal) => signal.includes(E_G[0]))) {
      signalMap[E_G[0]] = "g";
      signalMap[E_G[1]] = "e";
    } else {
      signalMap[E_G[0]] = "e";
      signalMap[E_G[1]] = "g";
    }

    //convert the output
    let output4digit = "";
    for (output of entry["output"]) {
      let convertedOutput = [];
      for (char of output) {
        convertedOutput.push(signalMap[char]);
      }
      convertedOutput.sort();
      convertedOutput = convertedOutput.join("");

      output4digit += segmentsToNumbers[convertedOutput];
    }

    allOutputs.push(Number(output4digit));
  }

  return allOutputs.reduce((sum, v) => sum + v);
};

console.log(`Solution 01: ${solution1(inputData)}`);
console.log(`Solution 02: ${solution2(inputData)}`);
