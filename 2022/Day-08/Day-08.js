const fs = require("fs");

inputData = fs.readFileSync("input.txt", "utf8");
inputData = inputData
  .split(/\r?\n/)
  .map((line) => line.split("").map((v) => Number(v)));

const transposeArray = (array) =>
  array[0].map((_, i) => array.map((row) => row[i]));

const solution = (treeMap, part) => {
  const treeMapTransposed = transposeArray(treeMap);

  const width = treeMap[0].length;
  const height = treeMap.length;

  let visibleCounter = 0;
  let maxScenicScore = 0;

  for (let y = 0; y < height; y++) {
    for (let x = 0; x < width; x++) {
      const currTree = treeMap[y][x];

      const treesToCompareAllDirections = [
        //left,right,top,bottom
        treeMap[y].slice(0, x).reverse(),
        treeMap[y].slice(x + 1),
        treeMapTransposed[x].slice(0, y).reverse(),
        treeMapTransposed[x].slice(y + 1),
      ];

      //part 1
      if (part === 1) {
        for (let treesToCompare of treesToCompareAllDirections) {
          if (currTree > Math.max(...treesToCompare)) {
            visibleCounter++;
            break;
          }
        }

        //part 2
      } else if (part === 2) {
        let currTreeScenicScore = [];

        for (let treesToCompare of treesToCompareAllDirections) {
          if (!treesToCompare.length) {
            currTreeScenicScore.push(0);
            continue;
          }

          for (let [i, treeToCompare] of treesToCompare.entries()) {
            if (treeToCompare >= currTree || i === treesToCompare.length - 1) {
              currTreeScenicScore.push(i + 1);
              break;
            }
          }
        }

        maxScenicScore = Math.max(
          maxScenicScore,
          currTreeScenicScore.reduce((a, b) => a * b)
        );
      }
    }
  }

  return part === 1 ? visibleCounter : maxScenicScore;
};

console.log(`Solution 01: ${solution(inputData, 1)}`);
console.log(`Solution 02: ${solution(inputData, 2)}`);
