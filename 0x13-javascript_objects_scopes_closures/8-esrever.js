#!/usr/bin/node

exports.esrever = function (list) {
  const revList = [];
  for (let len = list.length, i = 0; len > 0; len--, i++) {
    revList[j] = list[i - 1];
  }

  return revList;
};
