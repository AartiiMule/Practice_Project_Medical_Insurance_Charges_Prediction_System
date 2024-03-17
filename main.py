
from flask import Flask, jsonify, render_template, request

from project_app.utils import MedicalInsurance

# Creating instance here
app = Flask(__name__)


@app.route("/") 
def hello_flask():
    print("Welcome to Insurance Prediction System")   
    return render_template("index.html")


@app.route("/predict_charges", methods = ["POST", "GET"])
def get_insurance_charges():
    if request.method == "GET":
        print("We are in a GET Method")

        # data = request.form
        # print("Data -->\n",data)

        # age = eval(data['age'])
        # sex = data['sex']
        # bmi = eval(data['bmi'])
        # children = eval(data['children'])
        # smoker = data['smoker'] region = data['region']

        age = int(request.args.get("age"))
        sex = request.args.get("sex")
        bmi = float(request.args.get("bmi"))
        children = int(request.args.get("children"))
        smoker = request.args.get("smoker")
        region = request.args.get("region") 

        print("*********************** age, sex, bmi, children, smoker, region **********************\n",age, sex, bmi, children, smoker, region)

        med_ins = MedicalInsurance(age, sex, bmi, children, smoker, region)
        charges = med_ins.get_predicted_charges()
        
        return render_template("index.html", prediction = charges)
    # return jsonify({"Result": f"Predicted Charges is {charges} /- Rs."})

print("__name__ -->", __name__)

if __name__ == "__main__":
    app.run(host= "0.0.0.0", port= 5005, debug = False)  # By default Prameters