const fs = require("fs");

const opponentDecryption = {
  A: "rock",
  B: "paper",
  C: "scissors",
};

const col2DecryptionPart01 = {
  X: "rock",
  Y: "paper",
  Z: "scissors",
};

const col2DecryptionPart02 = {
  X: "lose",
  Y: "draw",
  Z: "win",
};

const losingPairs = {
  rock: "scissors",
  paper: "rock",
  scissors: "paper",
};

const winningPairs = {
  rock: "paper",
  paper: "scissors",
  scissors: "rock",
};

const shapeToScore = {
  rock: 1,
  paper: 2,
  scissors: 3,
};

inputData = fs.readFileSync("input.txt", "utf8");
inputData = inputData.split(/\r?\n/);

inputData = inputData.map((v) => v.split(" "));

let roundsPart01 = [];
for (round of inputData) {
  roundsPart01.push({
    opponentShape: opponentDecryption[round[0]],
    myShape: col2DecryptionPart01[round[1]],
  });
}

let roundsPart02 = [];
for (round of inputData) {
  roundsPart02.push({
    opponentShape: opponentDecryption[round[0]],
    outcome: col2DecryptionPart02[round[1]],
  });
}

const Solution01 = (rounds) => {
  let score = 0;

  for (let round of rounds) {
    score += shapeToScore[round.myShape];

    if (round.opponentShape === round.myShape) {
      score += 3;
    }

    if (
      (round.myShape === "rock" && round.opponentShape == "scissors") ||
      (round.myShape === "paper" && round.opponentShape == "rock") ||
      (round.myShape === "scissors" && round.opponentShape == "paper")
    ) {
      score += 6;
    }
  }

  return score;
};

const Solution02 = (rounds) => {
  let score = 0;
  for (let round of rounds) {
    let myShape;

    if (round.outcome === "win") {
      score += 6;
      myShape = winningPairs[round.opponentShape];
    } else if (round.outcome === "lose") {
      myShape = losingPairs[round.opponentShape];
    } else {
      score += 3;
      myShape = round.opponentShape;
    }

    score += shapeToScore[myShape];
  }

  return score;
};

console.log(`Solution 01: ${Solution01(roundsPart01)}`);
console.log(`Solution 02: ${Solution02(roundsPart02)}`);
