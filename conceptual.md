### Conceptual Exercise

Answer the following questions below:

- What is RESTful routing?
  - Use standard HTTP verbs(GET, POST, PUT/PATCH,DELETE) and structures routes in a standardized way

- What is a resource?
  - An object with a type, associated data, relationships to other resources.

- When building a JSON API why do you not include routes to render a form that when submitted creates a new user?
  - It cannot represent SQLAlcehmy model instances

- What does idempotent mean? Which HTTP verbs are idempotent?
  - Idempotence refers to side-effects not all-effects or responses.
    - GET, PUT/PATCH, DELETE

- What is the difference between PUT and PATCH?
  - PUT - updates and entire resource
  - PATCH - updates part of a resource

- What is one way encryption?
  - non-reversible. same input always equals the same output

- What is the purpose of a `salt` when hashing a password?
  - allows for unique passwords even if two people use the same passwords

- What is the purpose of the Bcrypt module?
  - bcrypt module creates and stores hashed passwords

- What is the difference between authorization and authentication?
  - Authentication verifies the ID of the user and Authorization deteremines access rights
