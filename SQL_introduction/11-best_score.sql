-- a script that lists all records with a score >= 10 in the table second_table of the database hbtn_0c_0 in your MySQL server
SELECT score, name FROM second_table WHERE score >= 10 AND ORDER BY score DESC;
