from flask import Flask,redirect,url_for, request,render_template
import joblib
import numpy as np
 

app = Flask(__name__)
res=joblib.load('model.pkl')

@app.route('/')
def index():
    
    return render_template('page.html')

@app.route('/result', methods=['post'])
def login():
    if request.method == 'POST':
         weight = request.form["weight"]
         weight=int(weight)
         weight=res.predict([[weight]])
    return  render_template('page.html',val=weight)
   
if __name__ == '__main__':
   app.run(debug = True) 
