
DROP TABLE if exists Visits;

DROP TABLE IF EXISTS Transactions;

CREATE TABLE Visits (
    visit_id int PRIMARY KEY,
    customer_id int
);

CREATE TABLE Transactions (
    transaction_id int PRIMARY KEY,
    visit_id int,
    amount int
);

INSERT into Visits (
    visit_id,
    customer_id
) VALUES
(1, 23),
(2, 9),
(4, 30),
(5, 54),
(6, 96),
(7, 54),
(8, 54);

INSERT into Transactions (
    transaction_id,
    visit_id,
    amount
) VALUES
(2, 5, 310),
(3, 5, 300),
(9, 5, 200),
(12, 1, 910),
(13, 2, 970);


.headers on

SELECT
    v.customer_id,
    COUNT(v.customer_id) AS count_no_trans
FROM Visits v
    LEFT JOIN Transactions t
    ON v.visit_id = t.visit_id
    WHERE t.visit_id is NULL
    GROUP BY v.customer_id
;