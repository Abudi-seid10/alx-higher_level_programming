#!/usr/bin/node
const fs = require('fs');
const fileA = fs.readFileSync(process.argv[2]);
const fileB = fs.readFileSync(process.argv[3]);
const fileC = fs.createWriteStream(process.argv[4]);
const fileArray = [fileA, fileB];
fileArray.forEach(function (file) {
  fileC.write(file);
});
