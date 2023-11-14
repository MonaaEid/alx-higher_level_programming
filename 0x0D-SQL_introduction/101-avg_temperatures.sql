-- script that displays the average temperature (Fahrenheit) by city ordered by temperature (descending).
USE hbtn_0c_0;
SELECT city, AVG(temperature) AS average_temperature
FROM Temperatures
GROUP BY city
ORDER BY average_temperature DESC;
