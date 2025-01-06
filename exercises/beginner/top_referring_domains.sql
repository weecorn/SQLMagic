

-- Find the Top Referring Domains
-- You have a table called web_traffic with the following schema:

CREATE TABLE web_traffic (
    id SERIAL PRIMARY KEY,
    visit_date DATE,
    referrer_domain VARCHAR(255),
    page_views INT
);


-- Write a SQL query to identify the top 3 referring domains based on the total number of page_views in the last 6 months. If multiple domains have the same number of page_views, sort them alphabetically.
