const fs = require("fs");

inputData = fs.readFileSync("input.txt", "utf8");
inputData = inputData.split(/\r?\n/).map((line) => line.trim());

inputData.push("");

const monkeys = [];
let currMonkey = {};

const operate = (opA, opB, operator) => {
  switch (operator) {
    case "*":
      return opA * opB;
    case "+":
      return opA + opB;
  }
};

const oldOrNumber = (v) => {
  v = Number(v);
  if (isNaN(v)) {
    return "old";
  } else {
    return v;
  }
};

for (let line of inputData) {
  let [k, v] = line.split(": ");

  if (!k) {
    currMonkey.inspectionsCounter = 0;
    monkeys.push(currMonkey);
    currMonkey = {};
    continue;
  }

  switch (k) {
    case "Starting items":
      currMonkey.items = v.split(", ").map((v) => Number(v));
      break;
    case "Operation":
      v = v.split(" ").slice(2);
      currMonkey.operation = {};
      currMonkey.operation.opA = oldOrNumber(v[0]);
      currMonkey.operation.opB = oldOrNumber(v[2]);
      currMonkey.operation.operator = v[1];
      break;
    case "Test":
      v = Number(...v.split(" ").slice(-1));
      currMonkey.test = {};
      currMonkey.test.divisor = v;
      break;
    case "If true":
      v = Number(...v.split(" ").slice(-1));
      currMonkey.test.true = v;
      break;
    case "If false":
      v = Number(...v.split(" ").slice(-1));
      currMonkey.test.false = v;
      break;
  }
}

const solution01 = (monkeys) => {
  //loop round
  for (let round = 0; round < 20; round++) {
    //loop monkeys
    for (let monkey of monkeys) {
      for (let item of monkey.items) {
        monkey.inspectionsCounter++;

        //run the operation to update the value
        item = operate(
          monkey.operation.opA === "old" ? item : monkey.operation.opA,
          monkey.operation.opB === "old" ? item : monkey.operation.opB,
          monkey.operation.operator
        );
        item = Math.floor(item / 3);

        //test it
        if (item % monkey.test.divisor === 0) {
          monkeys[monkey.test.true].items.push(item);
        } else {
          monkeys[monkey.test.false].items.push(item);
        }
      }
      monkey.items = [];
    }
  }

  return monkeys
    .map((monkey) => monkey.inspectionsCounter)
    .sort((a, b) => b - a)
    .slice(0, 2)
    .reduce((acc, v) => acc * v);
};

console.log(`Solution 01: ${solution01(monkeys)}`);
