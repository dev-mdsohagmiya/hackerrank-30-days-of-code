const readline = require('readline');

const rl = readline.createInterface({
  input: process.stdin,
  output: process.stdout
});

rl.question('', (answer) => {
  const inputString = answer
  console.log("Hello, World.")
  console.log(inputString)
  rl.close();
});

// input will be hello