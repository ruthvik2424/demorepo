from flask import Flask, request, jsonify
from flask import Flask, request, jsonify
from flask import render_template
import json


app = Flask(__name__)
CORS = app


@app.route('/calculator', methods=['POST'])
def calculator():
    data = request.get_data()
    num1 = data['num1']
    num2 = data['num2']
    choice = data['choice']



    if choice == "+":
        r = n1 + n2
    elif choice == "-":
        r = n1 - n2
    elif choice == "*":
        r = n1 * n2
    elif choice == "/":
        r = n1 / n2
    elif choice == "**":
        r = n1 ** n2
    elif choice == "%":
        r = n1 % n2
    else:
        return jsonify({"error": "Invalid operator"})
    
    result = {
        "num1": n1,
        "num2": n2,
        "result": r
    }
    return jsonify({'result': result}), 200, {'Content-Type': 'application/json'}



@app.route('/home')
def home():
    return render_template('index.html')

if __name__ == "__main__":
    app.run()



