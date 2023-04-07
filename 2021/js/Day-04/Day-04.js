const fs = require("fs");

inputData = fs.readFileSync("input.txt", "utf8");

inputData = inputData.split(/\r?\n/).map((v) => v.trim());

// parse input data
let numbers = [],
  currentBoard = [],
  boards = [];

for (const [i, line] of inputData.entries()) {
  // console.log(i, inputData.length);

  //get the numbers
  if (i === 0) {
    for (const n of line.split(",")) {
      numbers.push(Number(n));
    }

    continue;
  }

  currentBoard.push(
    line
      .split(" ")
      .filter((v) => v) //remove empty entries
      .map((v) => Number(v))
  );

  //empty, or last, line pushed currentBoard to boards
  if (!line || i === inputData.length - 1) {
    if (!currentBoard.length) continue;

    if (currentBoard.length > 1) boards.push(currentBoard.slice(0, 5));
    currentBoard = [];
    continue;
  }
}

const transpose = (matrix) => {
  return matrix[0].map((col, i) => matrix.map((row) => row[i]));
};

const checkForWin = (board, calledNumbers) => {
  // console.log(board);
  for (const row of [...board, ...transpose(board)]) {
    if (row.every((v) => calledNumbers.includes(v))) {
      return true;
    }
  }

  return false;
};

const sumOfBoard = (board, calledNumbers) => {
  return board
    .flat()
    .reduce((sum, v) => (!calledNumbers.includes(v) ? sum + v : sum), 0);
};

const Solution01 = (numbers, boards) => {
  const findFirstWinner = (numbers, boards) => {
    let calledNumbers = [];

    //game loop
    for (const num of numbers) {
      calledNumbers.push(num);

      //check for winners
      for ([i, board] of boards.entries()) {
        const isWinner = checkForWin(board, calledNumbers);

        if (isWinner) {
          return [i, calledNumbers.at(-1), calledNumbers];
        }
      }
    }
  };

  //start the bingo
  const [winningBoardIndex, lastCalledNum, calledNumbers] = findFirstWinner(
    numbers,
    boards
  );

  const sumOfWinningBoard = sumOfBoard(
    boards[winningBoardIndex],
    calledNumbers
  );

  return sumOfWinningBoard * lastCalledNum;
};

const Solution02 = (numbers, boards) => {
  let calledNumbers = [];
  let winningBoards = [];
  let calledNumbersAtLastWin = [];
  let boardIndexAtLastWin;

  //game loop
  for (const num of numbers) {
    calledNumbers.push(num);

    //check for winners
    for ([i, board] of boards.entries()) {
      if (winningBoards.includes(i)) continue;

      const isWinner = checkForWin(board, calledNumbers);

      if (isWinner) {
        winningBoards.push(i);
        boardIndexAtLastWin = i;
        calledNumbersAtLastWin = [...calledNumbers];
      }
    }
  }

  const sumOfLastWinningBoard = sumOfBoard(
    boards[boardIndexAtLastWin],
    calledNumbersAtLastWin
  );

  return sumOfLastWinningBoard * calledNumbersAtLastWin.at(-1);
};

console.log(`Solution 01: ${Solution01(numbers, boards)}`);
console.log(`Solution 02: ${Solution02(numbers, boards)}`);
