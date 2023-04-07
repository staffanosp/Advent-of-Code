const deepCopy = (arr) => JSON.parse(JSON.stringify(arr));

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

const oldOrBigInt = (v) => {
  // v = Number(v);
  if (v === "old") {
    return v;
  } else {
    return BigInt(v);
  }
};

const logMonkeys = (monkeys) => {
  for (let [i, monkey] of monkeys.entries()) {
    console.log(monkey.items);
    console.log("inspectionsCounter", monkey.inspectionsCounter);
  }
};

const fs = require("fs");

inputData = fs.readFileSync("input.txt", "utf8");
inputData = inputData.split(/\r?\n/).map((line) => line.trim());

inputData.push("");

const monkeys = [];
let currMonkey = {};

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

const solution = (monkeys, part) => {
  let rounds = 0;
  if (part === 1) {
    rounds = 20;
  } else if (part === 2) {
    rounds = 10000;

    monkeys = monkeys.map((monkey) => {
      monkey.items = monkey.items.map((v) => BigInt(v));
      monkey.operation.opA = oldOrBigInt(monkey.operation.opA);
      monkey.operation.opB = oldOrBigInt(monkey.operation.opB);
      monkey.test.divisor = BigInt(monkey.test.divisor);
      // monkey.inspectionsCounter = BigInt(monkey.inspectionsCounter);

      return monkey;
    });

    logMonkeys(monkeys);
  }

  //loop round
  for (let round = 0; round < rounds; round++) {
    console.log("Round: ", round);
    //loop monkeys
    for (let monkey of monkeys) {
      for (let item of monkey.items) {
        console.log("count");
        monkey.inspectionsCounter++;

        //run the operation to update the value
        console.log("operate");
        console.log(
          `—————— Operation: ${
            monkey.operation.opA === "old" ? "old" : monkey.operation.opA
          } ${monkey.operation.operator} ${
            monkey.operation.opB === "old" ? "old" : monkey.operation.opB
          }`
        );

        if (
          part === 2 &&
          monkey.operation.opA === "old" &&
          monkey.operation.opB === "old" &&
          monkey.operation.operator === "*"
        ) {
          item = item ** 2n;
        } else {
          item = operate(
            monkey.operation.opA === "old" ? item : monkey.operation.opA,
            monkey.operation.opB === "old" ? item : monkey.operation.opB,
            monkey.operation.operator
          );
        }

        if (part === 1) {
          item = Math.floor(item / 3);
        }

        //test it
        console.log("test");
        if ([0, 0n].includes(item % monkey.test.divisor)) {
          console.log("———— Push");
          monkeys[monkey.test.true].items.push(item);
        } else {
          console.log("———— Push");
          monkeys[monkey.test.false].items.push(item);
        }
      }
      console.log("init array");
      monkey.items = [];
    }
  }

  return monkeys
    .map((monkey) => monkey.inspectionsCounter)
    .sort((a, b) => b - a)
    .slice(0, 2)
    .reduce((acc, v) => acc * v);
};

console.log(`Solution 01: ${solution(deepCopy(monkeys), 1)}`);
console.log(`Solution 02: ${solution(deepCopy(monkeys), 2)}`);

document.querySelectorAll(".box").forEach((x) => {
  x.addEventListener("click", (e) => {
    console.log(e);
  });
});
