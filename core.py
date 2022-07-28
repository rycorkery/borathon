from flask import Flask, request, abort
from CustomerAccount import CustomerAccount
import json

app = Flask(__name__)
customerAccounts = []
transactions = []

@app.route("/api/CustomerAccount/GetCustomerAccountByAccountNumber", methods = ["GET"])
def lookupAccount():
    id = int(request.args.get('id'))
    if id == None:
        abort(400, 'Insuffient ID specified.')
    for customerAccount in customerAccounts:
        print(customerAccount.id)
        if customerAccount.id == id:
            return json.dumps(customerAccount.__dict__)
    abort(400, "This ID was not found.")

@app.route("/api/CustomerAccount/OpenCustomerAccount", methods = ["POST"])
def openAccount():
    return

@app.route("/api/CustomerAccount/CloseCustomerAccount", methods = ["POST"])
def closeAccount():
    return

@app.route("/api/CustomerAccount/ApplyTransactionToCustomerAccount", methods = ["GET"])
def applyTransaction():
    return

if __name__ == "__main__":
    app.run()
