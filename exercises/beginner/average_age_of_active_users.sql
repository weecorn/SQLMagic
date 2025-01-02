-- PROBLEM
-- You have a table 'users' with the below schema, and data loaded
-- from dataset file signup_records_1000.csv

CREATE TABLE users (
    id SERIAL PRIMARY KEY,
    name VARCHAR(255),
    email VARCHAR(255),
    signup_date DATE,
    is_active BOOLEAN,
    age INT
);


-- Write a SQL query to find the average age of active users who signed up in the last 3 years.