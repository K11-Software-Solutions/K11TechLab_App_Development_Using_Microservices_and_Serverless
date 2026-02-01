# GraphQL City-State Microservice

This microservice provides a GraphQL API to return the US state for a given city, using UScities.json from the Lab2 folder.

## How to Run
1. Install dependencies:
   npm install
2. Start the server:
   node citystate_server.js
3. Access GraphQL playground:
   http://localhost:5030/graphql

## Example Query
```
{
  state(city: "Chicago")
}
```
