from flask import Flask, render_template, request
from project_app.utils import Titanic

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/predict_titanic", methods=["POST", "GET"])
def get_inputs():
    if request.method == "GET":
        try:
            # Pclass, Gender, Age, SibSp, Parch, Fare, Embarked
            Pclass = float(request.args.get("Pclass"))
            Gender = request.args.get("Gender")
            Age = float(request.args.get("Age"))
            SibSp = float(request.args.get("SibSp"))
            Parch = float(request.args.get("Parch"))
            Fare = float(request.args.get("Fare"))
            Embarked = request.args.get("Embarked")

            print("Pclass:", Pclass)
            print("Gender:", Gender)
            print("Age:", Age)
            print("SibSp:", SibSp)
            print("Parch:", Parch)
            print("Fare:", Fare)
            print("Embarked:", Embarked)

            titanic_test = Titanic(Pclass, Gender, Age, SibSp, Parch, Fare, Embarked)
            prediction = titanic_test.get_predicted_value()
  
            if prediction == 1:
                display_text = "Survived :)"
            else:
                display_text = "Not Survived :("
        except:
            display_text = "Error : Invalid Input"
    return render_template("index.html", prediction=display_text)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
