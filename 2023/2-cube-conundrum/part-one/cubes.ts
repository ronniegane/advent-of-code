import { readFileSync } from 'fs';

/*
To get information, once a bag has been loaded with cubes, the Elf will reach into the bag, grab a handful of random cubes, show them to you, and then put them back in the bag. He'll do this a few times per game.

You play several games and record the information from each game (your puzzle input). Each game is listed with its ID number (like the 11 in Game 11: ...) followed by a semicolon-separated list of subsets of cubes that were revealed from the bag (like 3 red, 5 green, 4 blue).

For example, the record of a few games might look like this:

Game 1: 3 blue, 4 red; 1 red, 2 green, 6 blue; 2 green
Game 2: 1 blue, 2 green; 3 green, 4 blue, 1 red; 1 green, 1 blue
Game 3: 8 green, 6 blue, 20 red; 5 blue, 4 red, 13 green; 5 green, 1 red
Game 4: 1 green, 3 red, 6 blue; 3 green, 6 red; 3 green, 15 blue, 14 red
Game 5: 6 red, 1 blue, 3 green; 2 blue, 1 red, 2 green
In game 1, three sets of cubes are revealed from the bag (and then put back again). The first set is 3 blue cubes and 4 red cubes; the second set is 1 red cube, 2 green cubes, and 6 blue cubes; the third set is only 2 green cubes.

The Elf would first like to know which games would have been possible if the bag contained only 12 red cubes, 13 green cubes, and 14 blue cubes?

In the example above, games 1, 2, and 5 would have been possible if the bag had been loaded with that configuration. However, game 3 would have been impossible because at one point the Elf showed you 20 red cubes at once; similarly, game 4 would also have been impossible because the Elf showed you 15 blue cubes at once. If you add up the IDs of the games that would have been possible, you get 8.

Determine which games would have been possible if the bag had been loaded with only 12 red cubes, 13 green cubes, and 14 blue cubes. What is the sum of the IDs of those games?
*/

const isPossible = (
  game: string,
  redMax: number,
  greenMax: number,
  blueMax: number,
) => {
  const maxColours: Record<string, number> = {
    red: redMax,
    green: greenMax,
    blue: blueMax,
  };
  const draws = game.split(';');
  for (const draw of draws) {
    // console.log(draw);
    const colours = draw.split(',');
    for (const colourCount of colours) {
      // console.log(colourCount);
      const [count, colour] = colourCount.trim().split(' ');
      // Check: no colour has more than its max
      // if (colour in maxColours) { // can we skip this type check??
      // console.log(`colour: ${colour}`);
      // console.log(`count: ${count}`);
      if (parseInt(count, 10) > maxColours[colour.trim()]) {
        return false;
      }
      // }
    }
  }
  return true;
};

const inputFile = process.argv[2]; // node script-file args
const input = readFileSync(inputFile, 'utf-8');

const red = 12;
const green = 13;
const blue = 14;

const possibleGames: number[] = [];
const impossibleGames: number[] = [];
let sumPossible = 0;

for (const line of input.trimEnd().split('\n')) {
  // each line is a game
  const [gameTitle, game] = line.split(':');

  const gameNumber = parseInt(gameTitle.split(' ')[1], 10);
  if (isPossible(game, red, green, blue)) {
    console.log(`${gameTitle} is possible`);
    possibleGames.push(gameNumber);
    sumPossible += gameNumber;
  } else {
    console.log(`${gameTitle} is not possible`);
    impossibleGames.push(gameNumber);
  }
}
console.log(`impossible: ${impossibleGames}`);
console.log(`possible: ${possibleGames}`);
console.log(`Sum of possible game IDs: ${sumPossible}`);
