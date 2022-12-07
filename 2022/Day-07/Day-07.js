const fs = require("fs");

inputData = fs.readFileSync("input.txt", "utf8");
inputData = inputData.split(/\r?\n/);

function convertPathArrayToString(path) {
  return path.join("/");
}

const pwd = [];
const files = [];
const dirs = [];

for (let line of inputData) {
  if (line[0] === "$") {
    //command
    line = line.slice(2).split(" ");
    const command = line[0];
    const arg = line[1];

    if (command === "cd") {
      if (arg === "..") {
        pwd.pop();
      } else {
        pwd.push(arg);

        const path = convertPathArrayToString(pwd);
        dirs.push({ path, size: 0 });
      }
    }
  } else {
    //file or dir
    line = line.split(" ");
    if (line[0] !== "dir") {
      //file
      const path = convertPathArrayToString([...pwd, line[1]]);
      const size = Number(line[0]);
      files.push({ path, size });
    }
  }
}

//size per folder
dirs.forEach((dir) => {
  dir.size = files
    .filter((file) => file.path.startsWith(dir.path))
    .reduce((sum, file) => sum + file.size, 0);
});

const solution01 = (dirs) => {
  return dirs
    .filter((dir) => dir.size < 100000)
    .reduce((sum, dir) => sum + dir.size, 0);
};

const solution02 = (dirs) => {
  const diskSpace = 70000000;
  const diskSpaceRequired = 30000000;
  const currentlyUsedDiskSpace = dirs[0].size;
  const currentlyFreeDiskSpace = diskSpace - currentlyUsedDiskSpace;
  const additionallyRequiredFreeSpace =
    diskSpaceRequired - currentlyFreeDiskSpace;

  return Math.min(
    ...dirs
      .map((dir) => dir.size)
      .filter((size) => size > additionallyRequiredFreeSpace)
  );
};

console.log(`Solution 01: ${solution01(dirs)}`);
console.log(`Solution 02: ${solution02(dirs)}`);
