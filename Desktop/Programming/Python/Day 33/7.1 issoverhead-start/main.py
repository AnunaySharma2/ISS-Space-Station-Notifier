import requests
import smtplib
import time
from datetime import datetime

MY_LAT = 23.259933  # Your latitude
MY_LONG = 77.412613  # Your longitude

response = requests.get(url="http://api.open-notify.org/iss-now.json")
response.raise_for_status()
data = response.json()

iss_latitude = float(data["iss_position"]["latitude"])
iss_longitude = float(data["iss_position"]["longitude"])

MY_MAIL = "ENTER YOUR ADDRESS"
PASSWORD = "ENTER MY_MAIL PASSWORD"
SENDERS_ADDRESS = "SENDERS ADDRESS"


def check_position():
    if abs(iss_longitude - MY_LONG) <= 5 and abs(iss_latitude - MY_LAT) <= 5:
        return True
    return False


def is_dark():
    if time_now.hour >= sunset or time_now.hour <= sunrise:
        return True
    return False


parameters = {
    "lat": MY_LAT,
    "lng": MY_LONG,
    "formatted": 0,
}

response = requests.get("https://api.sunrise-sunset.org/json", params=parameters)
response.raise_for_status()
data = response.json()
sunrise = int(data["results"]["sunrise"].split("T")[1].split(":")[0])
sunset = int(data["results"]["sunset"].split("T")[1].split(":")[0])

time_now = datetime.now()

# If the ISS is close to my current position
# and it is currently dark
# Then send me an email to tell me to look up.
# BONUS: run the code every 60 seconds.
while True:
    time.sleep(60)
    if is_dark() and check_position():
        with smtplib.SMTP("smtp.gmail.com") as connection:
            connection.starttls()
            connection.login(user=MY_MAIL, password=PASSWORD)
            connection.sendmail(from_addr=MY_MAIL, to_addrs=SENDERS_ADDRESS,
                                msg="Subject:Look up in the sky\n\nLook for ISS space station above in the sky")
