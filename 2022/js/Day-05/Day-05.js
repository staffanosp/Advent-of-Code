const fs = require("fs");

inputData = fs.readFileSync("input.txt", "utf8");
inputData = inputData.split(/\r?\n/);

//separate stacks and instructions
const stacksRaw = [];
let instructions = [];

let pass = 0;
for (let line of inputData) {
  if (!line) {
    pass++;
    continue;
  }

  if (pass === 0) {
    stacksRaw.push(line);
  } else if (pass === 1) {
    instructions.push(line);
  }
}

//convert the stacks input
stacksRaw.pop(); //get rid of last line

const stacks = [];
const numberOfStacks = (stacksRaw[0].length + 1) / 4;
for (let stack = 0; stack < numberOfStacks; stack++) {
  const currStack = [];
  const currIndex = 1 + 4 * stack;

  for (const line of stacksRaw) {
    const crate = line.charAt(currIndex).trim();

    if (crate) {
      currStack.unshift(crate);
    }
  }

  stacks.push(currStack);
}

//convert the instructions input
instructions = instructions
  .map((line) => line.split(" ").map((v) => Number(v)))
  .map((line) => line.filter((v) => !isNaN(v)));

const deepCopy = (arr) => JSON.parse(JSON.stringify(arr));

const Solution01 = (stacks, instructions) => {
  for (const instruction of instructions) {
    const toMoveCount = instruction[0];
    const from = instruction[1] - 1;
    const to = instruction[2] - 1;

    for (let i = 0; i < toMoveCount; i++) {
      stacks[to].push(stacks[from].pop());
    }
  }

  let topCrates = [];
  for (let stack of stacks) {
    topCrates.push(stack.pop());
  }

  return topCrates.join("");
};

const Solution02 = (stacks, instructions) => {
  for (const instruction of instructions) {
    const toMoveCount = instruction[0];
    const from = instruction[1] - 1;
    const to = instruction[2] - 1;

    const cratesToMove = stacks[from].splice(-toMoveCount);
    stacks[to].push(...cratesToMove);
  }

  let topCrates = [];
  for (let stack of stacks) {
    topCrates.push(stack.pop());
  }

  return topCrates.join("");
};

console.log(`Solution 01: ${Solution01(deepCopy(stacks), instructions)}`);
console.log(`Solution 02: ${Solution02(deepCopy(stacks), instructions)}`);
