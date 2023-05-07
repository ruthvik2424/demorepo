from flask import Flask, request, jsonify, render_template
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

@app.route("/calculate", methods=["POST"])
def calculate():
    try:
        # Get the request data as a JSON object
        formData = request.get_json()

        # Extract the values from the JSON object
        num1 = formData["num1"]
        num2 = formData["num2"]

        # Calculate the sum of the numbers
        result = num1 + num2

        # Return the result as a JSON object
        return jsonify({"result": result})

    except Exception as e:
        # Print out the error message and traceback information
        print("Error:", str(e))
        import traceback
        traceback.print_exc()
        return jsonify({"error": str(e)}), 500

@app.route('/html')
def page():
    return render_template('index.html')

if __name__ == "__main__":
    app.run(debug=True)

# from flask import Flask, request, jsonify
# from flask import render_template


# app = Flask(__name__)


# @app.route('/calculator', methods=['POST'])
# def calculator():
#     data = request.get_json()
#     num1 = data['num1']
#     num2 = data['num2']
#     choice = data['choice']
#     if (choice == "add"):
#                 result = {
#                     "num1": num1,
#                     "num2": num2,
#                     "result": num1 + num2
#                 }
#     elif(choice == "sub"):
#                 result = {
#                     "num1": num1,
#                     "num2": num2,
#                     "result": num1 - num2
#                 }
#     elif(choice == "mul"):
#                 result = {
#                     "num1": num1,
#                     "num2": num2,
#                     "result": num1 * num2
#                 }
#     elif(choice == "div"):
#                 result = {
#                     "num1": num1,
#                     "num2": num2,
#                     "result": num1 / num2
#                 }
#     elif(choice == "expo"):
#                 result = {
#                     "num1": num1,
#                     "num2": num2,
#                     "result": num1 ** num2
#                 }
#     elif(choice == "mod"):
#                 result = {
#                     "num1": num1,
#                     "num2": num2,
#                     "result": num1 % num2
#                 }
#     return jsonify(result)

        



# list=[]
# def calculator(num1, num2):
#     if(choice =='+'):
#         print(num1,"+",num2,"=",num1+num2)
#         output=num1+num2
#         list.append(output)
#     elif(choice=='-'):
#         print(num1,"-",num2,"=",num1-num2)
#         output=num1+num2
#         list.append(output)
#     elif(choice=='*'):
#         print(num1,"*",num2,"=",num1*num2)
#         output=num1+num2
#         list.append(output)
#     elif(choice=='/'):
#         print(num1,"/",num2,"=",num1/num2)
#         output=num1+num2
#         list.append(output)
#     elif(choice=='%'):
#         print(num1,"%",num2,"=",num1%num2)
#         output=num1+num2
#         list.append(output)  
#     else:
#         print("Please choose the correct option")  
    
# def table(num):
#      for i in range(1, 11):
#         print(num, "x" ,i, "=" ,num * i,)
# print("\t\tSimple Calculator")

