#!/usr/bin/node

const argCount = process.argv.length;
if (argCount <= 3) {
  console.log('0');
} else {
  const args = process.argv.slice(2);
  const nums = args.map(Number);

  nums.sort(function (a, b) { return (b - a); });

  console.log(nums[1]);
}
