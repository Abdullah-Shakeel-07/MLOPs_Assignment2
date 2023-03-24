from flask import Flask,request, render_template
import pickle
from datetime import datetime
import numpy as np
# import pandas as pd
# from sklearn.metrics import mean_absolute_error
# from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression

app = Flask(__name__)

model=pickle.load(open('model.pkl','rb'))


@app.route('/')
def hello_world():
    return render_template("frontend.html")


@app.route('/predict',methods=['POST','GET'])
def predict():
    int_features=[float(x) for x in request.form.values()]
    final=np.array(int_features)
    y_pred = model.predict(final.reshape(1, -1))
    # print(int(y_pred))
    return render_template('frontend.html',pred='Predcited price is {}'.format(y_pred))


if __name__ == '__main__':
    app.run(debug=False)