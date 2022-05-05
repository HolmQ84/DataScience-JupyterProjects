
# Import libraries
import numpy as np
import pandas as pd
import json
import plotly
import plotly.express as px

# from sklearn.externals 
import joblib
import pickle
from flask import Flask, request, jsonify, render_template

# create an instance (our app)
app = Flask(__name__, template_folder='../templates')
# app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])

@app.route('/hi/<name>')
def hello(name = None):
    return render_template('start.html', name=name)
# name is parameter in the template: {{name}}

@app.route('/predict')
def predict():
    return render_template('prediction.html')

@app.route('/predicted', methods=['GET', 'POST'])
def predicted():
    if request.method == 'POST':
        x1 = request.form['x1']
        x2 = request.form['x2']
        X = [[x1, x2]]
        predicted = msmodel.predict(X)
          
        return render_template("predicted.html", content=X, prediction=predicted)
    
@app.route('/bye')
def bye():
    return render_template('bye.html')

@app.route('/test')
def notdash():
   df = pd.DataFrame({
      'Fruit': ['Apples', 'Oranges', 'Bananas', 'Apples', 'Oranges', 
      'Bananas'],
      'Amount': [4, 1, 2, 2, 4, 5],
      'City': ['SF', 'SF', 'SF', 'Montreal', 'Montreal', 'Montreal']
   })
   fig = px.bar(df, x='Fruit', y='Amount', color='City', 
      barmode='group')
   graphJSON = json.dumps(fig, cls=plotly.utils.PlotlyJSONEncoder)
   return render_template('flaskpytest.html', graphJSON=graphJSON)

@app.route('/setValues')
def setValues():
    return render_template('setValues.html')

@app.route('/getCharts', methods=['GET', 'POST'])
def getCharts():
    if request.method == 'POST':
        value1name = request.form['value1name']
        value2name = request.form['value2name']
        value3name = request.form['value3name']
        value4name = request.form['value4name']
        value1amount = request.form['value1amount']
        value2amount = request.form['value2amount']
        value3amount = request.form['value3amount']
        value4amount = request.form['value4amount']
        
        names = [value1name, value2name, value3name, value4name]
        amounts = [value1amount, value2amount, value3amount, value4amount]
        
        df = pd.DataFrame({
            'Name': names,
            'Amount': amounts
        })
        fig2 = px.pie(df, values='Amount', names='Name')
        graphJSON2 = json.dumps(fig2, cls=plotly.utils.PlotlyJSONEncoder)
        return render_template("getCharts.html", graphJSON=graphJSON2)

if __name__ == '__main__':
    app.run(debug=True)
