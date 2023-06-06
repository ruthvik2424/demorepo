import requests
import json

url = "http://127.0.0.1:5000/calculate"


oper = input("enter the operation")
num1 = int(input("enter the first number"))
num2 = int(input("enter the second number"))

data = json.dumps({"num1": num1, "num2": num2, "choice": oper})

headers = {"Content-Type": "application/json"}

response = requests.post(url, data=data, headers=headers)

result = json.loads(response.content)

print(result)