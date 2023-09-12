#!/usr/bin/node

function factorial (a) {
  if (isNaN(a)) {
    console.log(1);
  } else {
    let fact = 1;
    for (let i = a; i > 0; i--) {
      fact *= i;
    }
    console.log(a);
  }
}

const arg = process.argv[2];

factorial(arg);
