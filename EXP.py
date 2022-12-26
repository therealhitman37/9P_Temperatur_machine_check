import requests
import time

# URL of the machine
url = "http://machine.com/temperature"

# Desired temperature range
low = 20
high = 25

# Check the temperature every 60 seconds
while True:
  # Make a GET request to the machine's URL to get the current temperature
  response = requests.get(url)

  # Check if the request was successful
  if response.status_code == 200:
    # Convert the response text to a float
    temperature = float(response.text)

    # Check if the temperature is within the desired range
    if temperature >= low and temperature <= high:
      print("Temperature is within range")
    else:
      print("Temperature is outside of range")
  else:
    print("Failed to get temperature from machine")

  # Wait 60 seconds before checking the temperature again
  time.sleep(60)


