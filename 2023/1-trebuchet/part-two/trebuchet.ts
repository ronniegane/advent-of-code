import { readFileSync } from 'fs';
/*
Your calculation isn't quite right. It looks like some of the digits are actually spelled out with letters: one, two, three, four, five, six, seven, eight, and nine also count as valid "digits".

Equipped with this new information, you now need to find the real first and last digit on each line. For example:

two1nine
eightwothree
abcone2threexyz
xtwone3four
4nineeightseven2
zoneight234
7pqrstsixteen
In this example, the calibration values are 29, 83, 13, 24, 42, 14, and 76. Adding these together produces 281.

NOTE:
careful for overlapping text numbers e.g. sevenineightwone
because of this, safer to just increment one space rather than trying to skip ahead.
*/

const getDigits = (line: string) => {
  let a: number | undefined;
  let b: number | undefined;
  for (let i = 0; i < line.length; i++) {
    const c = line[i];

    switch (c) {
      case '1':
      case '2':
      case '3':
      case '4':
      case '5':
      case '6':
      case '7':
      case '8':
      case '9':
        b = parseInt(c, 10);
        break;
      case 'o':
        // one
        if (line.substring(i, i + 3) === 'one') {
          b = 1;
        }
        break;
      case 't':
        // two or three
        if (line.substring(i, i + 3) === 'two') {
          b = 2;
        } else if (line.substring(i, i + 5) === 'three') {
          b = 3;
        }
        break;
      case 'f':
        // four or five
        if (line.substring(i, i + 4) === 'four') {
          b = 4;
        } else if (line.substring(i, i + 4) === 'five') {
          b = 5;
        }
        break;
      case 's':
        // six or seven
        if (line.substring(i, i + 3) === 'six') {
          b = 6;
        } else if (line.substring(i, i + 5) === 'seven') {
          b = 7;
        }
        break;
      case 'e':
        // eight
        if (line.substring(i, i + 5) === 'eight') {
          b = 8;
        }
        break;
      case 'n':
        // nine
        if (line.substring(i, i + 4) === 'nine') {
          b = 9;
        }
        break;
      default:
        break;
    }
    if (a == undefined) {
      a = b;
    }
  }

  if (a == undefined || b == undefined) {
    throw new Error('did not find any numbers');
  }
  return a * 10 + b;
};

// const input = readFileSync('./tricky-input.txt', 'utf-8');
const input = readFileSync('../part-one/input.txt', 'utf-8');
// const input = readFileSync('./test-input.txt', 'utf-8');

let sum = 0;

for (const line of input.trimEnd().split('\n')) {
  const lineValue = getDigits(line);
  console.log(`${lineValue} | ${line}`);
  sum += getDigits(line);
}
console.log(sum);
