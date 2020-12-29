import pickle
import json
import numpy as np
import os

#__locations = None
#__data_columns = None
#__model = None

__loanamount = None
__model = None
__data_columns = None
__loanstatus = None

def get_loan_status(gender,married,education,self_employed,applicant_income,coapplicant_income,loan_amount,loan_amount_term,credit_history,property_area,dependents):
    print("values passed in get loan status - util")
    print(gender,married,education,self_employed,applicant_income,coapplicant_income,loan_amount,loan_amount_term,credit_history,property_area,dependents)
    if (loan_amount<0):
        loan_amount=0
    if (applicant_income<0):
        applicant_income = 0
    if(coapplicant_income<0):
        coapplicant_income=0
    x = np.zeros(len(__data_columns))
    x[0] = gender
    x[1] = married   
    x[2] = education
    x[3] = self_employed
    x[4] = applicant_income
    x[5] = coapplicant_income
    x[6] = loan_amount
    x[7] = loan_amount_term
    x[8] = credit_history
    x[9] = property_area
    x[10] = dependents

    status = __model.predict([x])[0]
    print("status: ",status)
    if status == 0:
        return "Rejected" 
    else:
        return "Approved"



def load_saved_artifacts():
    print("loading saved artifacts...start")
    global  __data_columns
    global __locations

    path = os.path.dirname(__file__) 
    artifacts = os.path.join(path, "artifacts"),

    with open(artifacts[0]+"/columns.json", "r") as f:
        __data_columns = json.load(f)['data_columns']
        #__locations = __data_columns[3:]  # first 3 columns are sqft, bath, bhk'''

    global __model
    if __model is None:
        with open(artifacts[0]+"/Pickle_Loan_Model.pkl", 'rb') as f:
            __model = pickle.load(f)
    print("loading saved artifacts...done")

'''def get_location_names():
    return __locations'''

def get_data_columns():
    return __data_columns

load_saved_artifacts()
print(get_loan_status(2,2,1,2,4547,0.0,115.0,360.0,1.0,2,0))
print(get_loan_status(2,1,1,2,4333,2451.0,110.0,360.0,1.0,3,0))