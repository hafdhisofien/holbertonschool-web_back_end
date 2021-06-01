import redis from 'redis';
const client = redis.createClient();

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

function displaySchoolValue(schoolName) {
    client.get(schoolName, function(error, reply) {
        console.log(reply);
    });
}


displaySchoolValue('Holberton');
setNewSchool('HolbertonSanFrancisco', '100');
displaySchoolValue('HolbertonSanFrancisco');
