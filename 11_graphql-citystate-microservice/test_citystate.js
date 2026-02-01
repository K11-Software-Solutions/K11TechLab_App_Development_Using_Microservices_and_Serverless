const fetch = require('node-fetch');
const fs = require('fs');

async function testStateQuery(cityName) {
  const query = `{
    state(city: "${cityName}")
  }`;
  const response = await fetch('http://localhost:5030/graphql', {
    method: 'POST',
    headers: { 'Content-Type': 'application/json' },
    body: JSON.stringify({ query })
  });
  const data = await response.json();
  fs.writeFileSync(`result_state_${cityName.replace(/ /g, '_').toLowerCase()}.json`, JSON.stringify(data, null, 2));
  console.log(`State query result for ${cityName} saved.`);
}

(async () => {
  for (const city of ['New York', 'Chicago', 'Los Angeles']) {
    await testStateQuery(city);
  }
})();
