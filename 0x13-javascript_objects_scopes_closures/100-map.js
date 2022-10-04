#!/usr/bin/node
const arrayInit = require('./100-data').list;

const newArray = arrayInit.map(function (element, index) {
  return (element * index);
});

console.log(arrayInit);
console.log(newArray);
