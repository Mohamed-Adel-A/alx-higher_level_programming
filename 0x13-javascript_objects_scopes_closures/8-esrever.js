#!/usr/bin/node

exports.esrever = function (list) {
  const revList = [];
  let len = list.length;
  for (let i = 0; len > 0; len--, i++) {
    revList[i] = list[len - 1];
  }

  return revList;
};
