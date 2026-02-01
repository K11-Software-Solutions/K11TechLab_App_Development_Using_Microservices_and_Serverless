# REST API and GraphQL Overview

## REST API
REST (Representational State Transfer) is an architectural style for designing networked applications. It uses HTTP requests to access and manipulate data, typically in JSON format. REST APIs are stateless, scalable, and easy to use. Each resource is identified by a URL, and standard HTTP methods (GET, POST, PUT, DELETE) are used for operations.

**Advantages:**
- Simple and widely adopted
- Uses standard HTTP methods
- Easy to cache responses

**Disadvantages:**
- Can result in over-fetching or under-fetching of data
- Multiple endpoints may be needed for complex queries

## GraphQL
GraphQL is a query language for APIs and a runtime for executing those queries. It allows clients to request exactly the data they need, reducing over-fetching and under-fetching. GraphQL APIs expose a single endpoint and use a schema to define the types and relationships of data.

**Advantages:**
- Flexible queries (clients specify required fields)
- Reduces number of requests
- Strongly typed schema

**Disadvantages:**
- More complex to implement
- Requires learning new syntax

## REST vs GraphQL
| Feature         | REST API                | GraphQL                |
|----------------|------------------------|------------------------|
| Endpoints      | Multiple               | Single                 |
| Data Fetching  | Fixed per endpoint     | Flexible per query     |
| Over-fetching  | Possible               | Avoided                |
| Under-fetching | Possible               | Avoided                |
| Caching        | Easy                   | More complex           |
| Error Handling | Standard HTTP codes    | Custom error objects   |

## Use Cases
- **REST API:** Simple CRUD operations, public APIs, when caching is important.
- **GraphQL:** Complex data requirements, mobile apps, when clients need flexibility.

---

For more details, see the examples in the REST_API_AND_GraphQL directory.