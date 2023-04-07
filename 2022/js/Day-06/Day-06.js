const fs = require("fs");

inputData = fs.readFileSync("input.txt", "utf8");
inputData = inputData.trim().split("");

const findMarker = (inputData, markerLength) => {
  const buffer = [];
  for (let i = 0; i < inputData.length; i++) {
    buffer.push(inputData[i]);

    if (buffer.length < markerLength) continue;

    if (new Set(buffer).size === markerLength) {
      return i + 1;
    }

    buffer.shift();
  }
};

console.log(`Solution 01: ${findMarker(inputData, 4)}`);
console.log(`Solution 02: ${findMarker(inputData, 14)}`);
