# Write your MySQL query statement below
SELECT E.name, IFNULL(Em.unique_id, NULL) AS unique_id FROM Employees E LEFT JOIN EmployeeUNI Em ON E.id=Em.id;