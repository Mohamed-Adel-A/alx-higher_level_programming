#!/usr/bin/node

argCount = process.argv.length;
if (argCount <= 2) {
  console.log(0);
} else {
  const args = process.argv.slice(2);
  const nums = args.map(Number);

  nums.sort(function (a, b) {return (b - a);});

  console.log(nums[1]);
}
