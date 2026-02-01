# GraphQL Cities Microservice

This microservice provides a GraphQL API to query US cities data.

## How to Run
1. Install dependencies:
   npm install
2. Start the server:
   node graphserver.js
3. Access GraphQL playground:
   http://localhost:5020/graphql

## Example Queries
```
# Get all cities
{
  cities {
    name
    state
    population
  }
}

# Get a city by name
{
  city(name: "Chicago") {
    name
    state
    population
  }
}
```
