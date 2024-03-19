#!/usr/bin/node
exports.esrever = function (list) {
  const array = [];
  while (list.length > 0) {
    array.push(list.pop());
  }
  return array;
};
