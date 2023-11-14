-- script that displays the top 3 of cities temperature during July and August ordered by temperature (descending)
SELECT city, AVG(temperature) AS average_temperature
FROM Temperatures
WHERE month IN (7, 8)
GROUP BY city
ORDER BY average_temperature DESC
LIMIT 3;
