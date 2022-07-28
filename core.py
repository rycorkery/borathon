from flask import Flask

app = Flask(__name__)
customerAccounts = []
transactions = []

@app.route("/api/CustomerAccount/GetCustomerAccountByAccountNumber", methods = ["GET"])
def lookupAccount():
    return

@app.route("/api/CustomerAccount/OpenCustomerAccount", methods = ["POST"])
def openAccount():
    return

@app.route("/api/CustomerAccount/CloseCustomerAccount", methods = ["POST"])
def closeAccount():
    return

@app.route("/api/CustomerAccount/ApplyTransactionToCustomerAccount", methods = ["GET"])
def applyTransaction():
    return
