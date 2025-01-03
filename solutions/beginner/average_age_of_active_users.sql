
-- SOLUTION
SELECT 
    ROUND(AVG(age), 2) AS average_age
FROM 
    users
WHERE 
    is_active = TRUE
    AND signup_date >= CURRENT_DATE - INTERVAL '3 years';


