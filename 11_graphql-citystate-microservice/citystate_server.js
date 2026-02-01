const express = require('express');
const { graphqlHTTP } = require('express-graphql');
const { buildSchema } = require('graphql');
const fs = require('fs');

// Load UScities.json from Lab2 folder
const cities = JSON.parse(fs.readFileSync('UScities.json'));

const schema = buildSchema(`
  type Query {
    state(city: String!): String
  }
`);

const root = {
  state: ({ city }) => {
    const found = cities.find(c => c.city && c.city.toLowerCase() === city.toLowerCase());
    return found ? found.state : null;
  }
};

const app = express();
app.use('/graphql', graphqlHTTP({
  schema: schema,
  rootValue: root,
  graphiql: true,
}));

app.listen(5030, () => {
  console.log('GraphQL City-State API running at http://localhost:5030/graphql');
});
