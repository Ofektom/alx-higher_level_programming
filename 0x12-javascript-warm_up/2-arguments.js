#!/usr/bin/node

const args = process.argv.slice(2);

let argCount = 0;

for (const arg of args) {
  argCount++;
}

if (argCount === 0) {
  console.log('No argument');
} else if (args.length === 1) {
  console.log('Argument found');
} else {
  console.log('Arguments found');
}
