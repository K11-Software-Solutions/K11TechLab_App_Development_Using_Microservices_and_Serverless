const fetch = require('node-fetch');
const fs = require('fs');

async function testCitiesQuery() {
  const query = `{
    cities {
      name
      state
      population
    }
  }`;
  const response = await fetch('http://localhost:5020/graphql', {
    method: 'POST',
    headers: { 'Content-Type': 'application/json' },
    body: JSON.stringify({ query })
  });
  const data = await response.json();
  fs.writeFileSync('result_cities.json', JSON.stringify(data, null, 2));
  console.log('Cities query result saved to result_cities.json');
}

async function testCityQuery(cityName) {
  const query = `{
    city(name: "${cityName}") {
      name
      state
      population
    }
  }`;
  const response = await fetch('http://localhost:5020/graphql', {
    method: 'POST',
    headers: { 'Content-Type': 'application/json' },
    body: JSON.stringify({ query })
  });
  const data = await response.json();
  fs.writeFileSync(`result_city_${cityName.replace(/ /g, '_').toLowerCase()}.json`, JSON.stringify(data, null, 2));
  console.log(`City query result for ${cityName} saved.`);
}

(async () => {
  await testCitiesQuery();
  for (const city of ['New York', 'Chicago']) {
    await testCityQuery(city);
  }
})();
