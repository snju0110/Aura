import requests

url = 'http://127.0.0.1:8000/foodlog/'

data_template = {  "user": "Sanjay", "time_stamp": "2023-02-10T18:21:36",
                 "meal_type": "Dinner",
                 "meal_qty": 3, "category": "non-veg", "junk": "yes",
                 "latitude": "1.1234500000", "longitude": "2.1234500000"
                   }

status = requests.post(url, json=data_template)

print(status.json())
