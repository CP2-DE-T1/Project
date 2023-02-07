import requests
import json
import random

def signup_api(id, gender, birth_date):
    url = "http://127.0.0.1:8000/api/users/sign-up/"
    headers = {'Content-Type': 'application/json', 'charset': 'UTF-8', 'Accept': '*/*'}
    body = {
        "username": f"test{id}",
        "name": "test",
        "email": f"test{id}@test.com",
        "password":"test",
        "password_check":"test",
        "gender":f"{gender}",
        "birth_date":f"{birth_date}"
    }
    
    try:
        response = requests.post(url, headers=headers, data=json.dumps(body, ensure_ascii=False, indent="\t"))
        print("response status %r" % response.status_code)
        print("response text %r" % response.text)
    except Exception as ex:
        print(ex)

def is_leapyear(year):
    if ((year % 4 == 0) and (year % 100 != 0)) or (year % 400 == 0):
        return True
    else:
        return False

def calculate_date():
    year = random.randint(1923,2022)
    month = random.randint(1,12)
    if month == 2:
        if is_leapyear(year):
            day = random.randint(1,29)
        else:
            day = random.randint(1,28)
    elif month in [1, 3, 5, 7, 8, 10, 12]:
        day = random.randint(1,31)
    else:
        day = random.randint(1, 30)
    
    if month < 10:
        month = str(month).zfill(2)

    if day < 10:
        day = str(day).zfill(2)

    return f"{year}-{month}-{day}"


for i in range(5000):
    birth_date = calculate_date()
    gender = random.choice(['Male', 'Female'])
    signup_api(i, gender, birth_date)