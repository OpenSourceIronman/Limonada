//run.js
var spawn = require('child_process').spawn,
    py    = spawn('python', ['read.py']),
    commands = [1,2,3,4,5,6,7,8,9],
    cmdString = '';

py.stdout.on('commands', function(commands){
  dataString += commands.toString();
});
py.stdout.on('end', function(){
  console.log('Sum of numbers=',dataString);
});
py.stdin.write(JSON.stringify(data));
py.stdin.end();