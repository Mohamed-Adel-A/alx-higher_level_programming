#!/usr/bin/node

argLenth = process.argv.lengthp;

if (argLenth === 2) {
  console.log('No argument');
} else if (argLenth === 3) {
  console.log('Argument found');
} else {
  console.log('Arguments found');
}
