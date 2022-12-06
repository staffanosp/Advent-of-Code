const fs = require("fs");

inputData = fs.readFileSync("input.txt", "utf8");
inputData = inputData.trim().split("");

const findMarker = (inputData, markerLength) => {
  let index = 0;

  while (true) {
    const currWindow = inputData.slice(index, index + markerLength);
    const currWindowUnique = new Set(currWindow);

    if (currWindow.length === currWindowUnique.size) {
      return index + markerLength;
    }

    index++;
  }
};

console.log(`Solution 01: ${findMarker(inputData, 4)}`);
console.log(`Solution 02: ${findMarker(inputData, 14)}`);
