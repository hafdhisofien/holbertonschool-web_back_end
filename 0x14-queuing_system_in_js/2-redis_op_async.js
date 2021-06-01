import redis from 'redis';
const client = redis.createClient();
const { promisify } = require("util");
const getAsync = promisify(client.get).bind(client);


client.on('connect', function() {
    console.log('Redis client connected to the server');
});

client.on('error', function(error) {
  console.error(`Redis client not connected to the server: ${error.message}`);
});

function setNewSchool(schoolName, value) {
    client.set(schoolName, value, function(error, reply){
        redis.print(`Reply: ${reply}`);
    });
}

async function displaySchoolValue(schoolName) {
    const reply = await getAsync(schoolName); 
        console.log(reply);
}


displaySchoolValue('Holberton');
setNewSchool('HolbertonSanFrancisco', '100');
displaySchoolValue('HolbertonSanFrancisco');
