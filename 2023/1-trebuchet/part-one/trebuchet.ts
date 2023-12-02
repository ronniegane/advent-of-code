import { readFileSync } from 'node:fs';

/*
The newly-improved calibration document consists of lines of text; each line originally contained a specific calibration value that the Elves now need to recover. On each line, the calibration value can be found by combining the first digit and the last digit (in that order) to form a single two-digit number.

For example:

1abc2
pqr3stu8vwx
a1b2c3d4e5f
treb7uchet
In this example, the calibration values of these four lines are 12, 38, 15, and 77. Adding these together produces 142.

Consider your entire calibration document. What is the sum of all of the calibration values?
*/

const getDigits = (line: string) => {
  let a: number | undefined;
  let b: number | undefined;
  for (let i = 0; i < line.length; i++) {
    // how to make sure we only go through the string once?
    const c = parseInt(line[i], 10);

    if (!Number.isNaN(c)) {
      if (!a) {
        // only assign this once
        a = c;
      }
      // always assign this so it will be the last one found
      b = c;
    }
  }

  if (a == undefined || b == undefined) {
    throw new Error('did not find any numbers');
  }
  return a * 10 + b;
};

const input = readFileSync('./input.txt', 'utf-8');

let sum = 0;

for (const line of input.trimEnd().split('\n')) {
  const lineValue = getDigits(line);
  console.log(`${lineValue} | ${line}`);
  sum += getDigits(line);
}
console.log(sum);
