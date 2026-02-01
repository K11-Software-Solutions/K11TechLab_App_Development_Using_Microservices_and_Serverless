const express = require('express');
const { graphqlHTTP } = require('express-graphql');
const { buildSchema } = require('graphql');
const fs = require('fs');

const cities = JSON.parse(fs.readFileSync('UScities.json'));

const schema = buildSchema(`
  type City {
    name: String
    state: String
    population: Int
  }
  type Query {
    cities: [City]
    city(name: String!): City
  }
`);

const root = {
  cities: () => cities,
  city: ({ name }) => cities.find(c => c.name.toLowerCase() === name.toLowerCase()),
};

const app = express();
app.use('/graphql', graphqlHTTP({
  schema: schema,
  rootValue: root,
  graphiql: true,
}));

app.listen(5020, () => {
  console.log('GraphQL Cities API running at http://localhost:5020/graphql');
});
