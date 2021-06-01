import redis from 'redis';
const client = redis.createClient();
const { promisify } = require("util");
const hgetall = promisify(client.hgetall).bind(client);

async function advOp() {
    const values = {
        Portland: 50,
        Seattle: 80,
        'New York': 20,
        Bogota: 20,
        Cali: 40,
        Paris: 2,
    };

    for (const value in values) {
        client.hset('HolbertonSchools', value, values[value], redis.print);
    }

    console.log(await hgetall('HolbertonSchools'));
}
advOp();