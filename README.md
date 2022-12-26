# 9P_Temperatur_machine_check
use Python to create a script that periodically checks the status of a machine or process and sends an alert if there is a problem.

1. The code begins by importing the requests library, which is used to make HTTP requests to URLs.

2. Next, it defines the URL of the machine and the desired temperature range.

3. The code then enters a loop that makes a GET request to the machine's URL using the requests.get() function. It stores the response in a variable called response.

4. The code checks if the request was successful by checking the value of response.status_code. If it is equal to 200, the request was successful and the code continues to the next step. Otherwise, it prints an error message.

5. If the request was successful, the code converts the response text to a float using the float() function and stores it in a variable called temperature.

6. Finally, the code checks if the temperature is within the desired range by comparing it to the low and high values. If it is within the range, it prints "Temperature is within range". If it is outside of the range, it prints "Temperature is outside of range".







