#!/usr/bin/node

const arg = process.argv[2];

if (isNaN(arg)) {
  console.log(1);
} else {
  let fact = 1;
  for (let i = arg; i > 0; i--) {
    fact *= i;
  }
  console.log(fact);
}
  
