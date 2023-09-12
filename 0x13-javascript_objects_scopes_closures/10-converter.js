#!/usr/bin/node

exports.converter = function (base) {
  return function (numberBase10) {
    return numberBase10.toString(base);
  };
};
