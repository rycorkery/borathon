from flask import Flask, request, abort
from CustomerAccount import CustomerAccount
import json
from Transaction import Transaction

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
    account_number = request.json['account_number']

    for customerAccount in customerAccounts:
        if customerAccount.account_number == account_number:
            customerAccount.status = 0
            return json.dumps(customerAccount.__dict__)

    abort(400, 'Account number not found.')

@app.route("/api/CustomerAccount/ApplyTransactionToCustomerAccount", methods = ["GET"])
def applyTransaction():
    if 'accountNumber' not in request.json or not request.json['accountNumber'].isnumeric():
        abort(400, 'Invalid account number')
    if 'amount' not in request.json or not request.json['amount'].isnumeric():
        abort(400, 'Invalid amount')
    if 'transactionType' not in request.json or (request.json['transactionType'] != '1' and request.json['transactionType'] != '2'):
        abort(400, 'Invalid transaction type')

    acc_number = request.json['accountNumber']
    amount = request.json['amount']
    trans_type = request.json['transactionType']

    t = Transaction(1, amount, acc_number, trans_type)
    t.save()
    # Save transaction
    transactions.append(t)

    # Find appropriate customer account
    found_customer_acc = customerAccounts[0]
    found_customer_acc.balance += amount
    # Save customer account

    return ''

if __name__ == "__main__":
    app.run(debug=True)
