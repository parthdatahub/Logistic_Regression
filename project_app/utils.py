import pandas as pd
import numpy as np
import pickle
import json
import os

class Titanic:
    def __init__(self, Pclass,Gender,Age,SibSp,Parch,Fare,Embarked):
        self.Pclass = Pclass
        self.Gender = Gender
        self.Age = Age
        self.SibSp = SibSp
        self.Parch = Parch
        self.Fare = Fare
        self.Embarked = Embarked
        
    def load_model(self):
        model_file_path = os.path.join(os.path.dirname(__file__),"logistic_Model3.pkl")
        json_file_path = os.path.join(os.path.dirname(__file__),"project_data.json")

        with open(model_file_path,"rb") as f:
            self.model = pickle.load(f)

        with open(json_file_path,"r") as f:
            self.json_data = json.load(f)
            self.feature_names = self.json_data["Columns"]

            # Assign feature names to the model
            self.model.feature_names = self.feature_names
    
    def get_predicted_value(self):
        self.load_model()

        #test_array=np.zeros(len("Columns"))
        test_array = np.zeros(len(self.json_data["Columns"]))
        test_array[0]=self.Pclass
        test_array[1]=self.json_data["Gender"][self.Gender]
        test_array[2]=self.Age
        test_array[3]=self.SibSp
        test_array[4]=self.Parch
        test_array[5]=self.Fare
        test_array[6]=self.json_data["Embarked"][self.Embarked]

        prediction = self.model.predict([test_array])[0]
        return prediction
    
if __name__== "__main__":
    Pclass=1.0000
    Gender="male"
    Age=32.0000
    SibSp=0.0000
    Parch=0.0000
    Fare=76.2917
    Embarked="C"
    
    obj_t=Titanic(Pclass,Gender,Age,SibSp,Parch,Fare,Embarked)
    prediction = obj_t.get_predicted_value()
    print("Prediction parth:",prediction) 