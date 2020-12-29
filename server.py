
from flask import Flask, request, jsonify, render_template
import server.util as util  #replace this by import util for running locally
#import util
import sys

app = Flask(__name__, static_url_path="/client", static_folder='../client', template_folder="../client")


@app.route('/', methods=['GET'])
def index():
    if request.method=="GET":
        return render_template("test1.html")

'''
@app.route('/get_location_names', methods=['GET'])
def get_location_names():
    response = jsonify({
        'locations': util.get_location_names()
    })
    response.headers.add('Access-Control-Allow-Origin', '*')
    return response'''

@app.route('/predict_loan_status', methods=['POST'])
def predict_loan_status():
    print("Loan starting here")
    gender = int(request.form['gender'])
    married = int(request.form['married'])
    education =int(request.form['education'])
    selfemployed = int(request.form['selfemployed'])
    applicantincome = int(request.form['applicantincome'])
    coapplicantincome = float(request.form['coapplicantincome'])
    loanamount = float(request.form['loanamount'])
    loanamountterm = float(request.form['loanamountterm'])
    credithistory = float(request.form['credithistory'])
    propertyarea = int(request.form['propertyarea'])
    dependents = int(request.form['dependents'])

    try:
        print("gender: ", gender)
        print("applicantincome: ",applicantincome)
        print("coapplicantincome: ",coapplicantincome)
        print("loanamount: ",loanamount)
        print("credithistory: ",credithistory)
        print("propertyarea: ", propertyarea)
        print("dependents: ",dependents)
        response = jsonify({'loan_status': util.get_loan_status(gender,married,education,selfemployed,applicantincome,
            coapplicantincome,loanamount,loanamountterm,credithistory,propertyarea,dependents)})        
    except:
        e = sys.exc_info()[0]
        print("Unexpected error:", e)
        response = jsonify({'loan_status': 'Error in getting response'})

    response.headers.add('Access-Control-Allow-Origin', '*')
    print("Added access control")
    return response

@app.route('/')
def Hi():
    return "Hi Uma"

if __name__ == "__main__":
    print("Starting Python Flask Server For Loan Status Prediction...")
    app.run(debug=True)


