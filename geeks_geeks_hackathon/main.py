import array
from flask import Flask,request,render_template
import pickle
import pandas as pd
import numpy as np

app  = Flask(__name__)

file = open("trained_model.pkl","rb")
model = pickle.load(file)
import numpy as np
# array = np.array([60,55,44,23.00445915,82.3207629,7.840207144,263.9642476])
# array = array.reshape(1,-1)
@app.route("/")

def home():
    return render_template("main.html")

@app.route("/predict",methods=['POST'])
def predict():
    input_feature = [[float(request.form.get("Nitrogen")),float(request.form.get("Phosphorous")),float(request.form.get("Potassium")),float(request.form.get("Temperature"))
                     ,float(request.form.get("Humidity")),float(request.form.get("Ph")),float(request.form.get("Rainfall"))]]
    print(input_feature)
    a = model.predict(input_feature)
    return render_template("main.html", jk = a)

if __name__ == "__main__":
    # app.run(debug=False)
    app.run(host = "0.0.0.0", debug=True, threaded=False)



import pickle
#
#
# p = model.predict(dd)
# print(p)