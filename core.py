from flask import request, abort
from CustomerAccount import CustomerAccount
import json
from Transaction import Transaction
from sqlalchemy import create_engine

from app import get_app_db

customerAccounts = []
transactions = []
latest_account_number = 0

app, db = get_app_db()

@app.route("/api/CustomerAccount/GetCustomerAccountByAccountNumber", methods = ["GET"])
def lookupAccount():
    id = int(request.args.get('id'))
    if id == None:
        abort(400, 'Insuffient ID specified.')
    customer = CustomerAccount.query.get(id)
    if customer != None:
        return json.dumps(customerAccount.__dict__)
    abort(400, "This ID was not found.")

@app.route("/api/CustomerAccount/OpenCustomerAccount", methods = ["POST"])
def openAccount():
    global latest_account_number

    # extract first and last name
    first_name = request.json['firstName']
    last_name = request.json['lastName']

    # first and last name validation
    if (not isinstance(first_name, str)) or (not isinstance(last_name, str)):
        abort(400, "First name or Last name are not strings")
    if (not first_name.isalpha()) or (not last_name.isalpha()):
        abort(400, "No spaces allowed in first or last name")

    # auto-incrementing account number
    latest_account_number += 1

    # save the account
    customer_account = CustomerAccount(
        latest_account_number,
        str(latest_account_number),
        0.0,
        1,
        first_name,
        last_name
    )
    db.session.add(customer_account)
    db.session.commit()

    # quering Customer Accounts to see if customer account
    # has been added to the database
    customer_accounts = CustomerAccount.query.all()
    for ca in customer_accounts:
        print(ca.first_name)
    return ""

@app.route("/api/CustomerAccount/CloseCustomerAccount", methods = ["POST"])
def closeAccount():
    account_number = request.json['account_number']
    
    customer_account = CustomerAccount.query.get(account_number)

    if customer_account != None:
        customer_account.staus = 0
        db.session.commit()
        return json.dumps(customer_account.__dict__)

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
    # upon restarting application, reset the DB
    db.drop_all()
    db.create_all()
    app.run(host='0.0.0.0')
