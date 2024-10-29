# Write your MySQL query statement below
-- SELECT V.customer_id, count(V.visit_id) AS count_no_trans FROM Visits V, Transactions T WHERE V.visit_id NOT IN
-- (
-- SELECT V.visit_id FROM Visits V, Transactions T WHERE V.visit_id=T.visit_id
-- )
-- GROUP BY V.customer_id;

SELECT V.customer_id, count(DISTINCT(V.visit_id)) AS count_no_trans FROM Visits V, Transactions T WHERE V.visit_id NOT IN
(
SELECT T.visit_id FROM Visits V, Transactions T WHERE V.visit_id=T.visit_id
)
GROUP BY V.customer_id;