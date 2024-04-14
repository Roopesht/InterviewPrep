### MongoDB Basics

#### 1. Installation
- Install MongoDB server and client on your machine. You can download it from the official MongoDB website.

#### 2. Starting MongoDB Server
- Start the MongoDB server using the command appropriate for your operating system (`mongod` command).

#### 3. Accessing MongoDB Shell
- Access the MongoDB shell using the `mongo` command. This is where you'll interact with the MongoDB database.

#### 4. Creating a Database
- Use the `use` command to create or switch to a specific database. If the database doesn't exist, MongoDB will create it when you first store data into it.

#### 5. Creating Collections
- Collections are analogous to tables in relational databases. You can create a collection implicitly by inserting documents into it or explicitly using the `createCollection` command.

#### 6. Inserting Documents
- Use the `insertOne` or `insertMany` methods to insert documents into a collection.

#### 7. Querying Data
- MongoDB provides various methods to query data:
  - **Basic Queries:** Use `find` to retrieve documents from a collection. You can specify query conditions to filter the result.
  - **Projection:** Use the second parameter of `find` to specify which fields to include or exclude in the result.
  - **Query Operators:** MongoDB provides a rich set of query operators such as `$eq`, `$gt`, `$lt`, `$in`, etc., to perform complex queries.
  - **Logical Operators:** MongoDB supports logical operators like `$and`, `$or`, `$not`, etc., to combine multiple conditions in a query.
  - **Sorting:** Use `sort` to sort the result based on one or more fields.
  - **Limit and Skip:** Use `limit` and `skip` to limit the number of documents returned and skip a specific number of documents, respectively.
  - **Aggregation:** MongoDB provides the `aggregate` method to perform aggregation operations like grouping, summing, averaging, etc., on the data.

#### 8. Updating Documents
- Use the `updateOne` or `updateMany` methods to update documents in a collection.

#### 9. Deleting Documents
- Use the `deleteOne` or `deleteMany` methods to delete documents from a collection.

#### 10. Indexing
- Indexes can improve the performance of queries by making them faster. You can create indexes on fields that are frequently used in queries.

#### 11. Schemaless Design
- MongoDB is schemaless, meaning you can store documents with different structures in the same collection. However, you should still have a well-defined schema for your data to maintain consistency.

#### 12. Backup and Restore
- MongoDB provides utilities like `mongodump` and `mongorestore` to backup and restore databases.

#### 13. Security
- Secure your MongoDB deployment by enabling authentication, setting up role-based access control, and enabling network encryption.

#### 14. Monitoring and Optimization
- Monitor your MongoDB deployment for performance issues and optimize queries and indexes as needed.

#### 15. Resources
- Refer to the official MongoDB documentation and online tutorials for more in-depth learning and best practices.
