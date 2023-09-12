#!/usr/bin/node

let arg_count = 0;

exports.logMe = function (item) {
  console.log(arg_count + ': ' + item);
  arg_count++;
};
