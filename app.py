from flask import Flask,redirect,render_template,request
import pickle
import numpy


app=Flask(__name__)
model=pickle.load(open('rf_healthcare.pkl','rb'))

@app.route('/')
def welcome():
    return render_template('index.html')

@app.route('/submit',methods=['POST'])
def submit():
    if request.method=="POST":
        pregnancies=int(request.form["pregnancies"])
        glucose=int(request.form["glucose"])
        bloodpressure=int(request.form["bloodpressure"])
        skinthickness=int(request.form["skinthickness"])
        insulin=int(request.form["insulin"])
        DiabetesPedigreeFunction=float(request.form["DiabetesPedigreeFunction"])
        bmi=float(request.form["bmi"])
        Age=int(request.form["Age"])
        
        result=model.predict([[pregnancies, glucose, bloodpressure, skinthickness, insulin, DiabetesPedigreeFunction, bmi, Age]])

    if result == 0:
        return render_template('index2.html')
    else:
        return render_template('index1.html')
   

if __name__=='__main__':
    app.run(debug=True)
