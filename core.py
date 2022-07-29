from flask import request, abort
from CustomerAccount import CustomerAccount
import json
from Transaction import Transaction
import uuid

from app import get_app_db

last_account_number = 0
app, db = get_app_db()

@app.route("/api/CustomerAccount/GetCustomerAccountByAccountNumber", methods = ["GET"])
def lookupAccount():
    id = int(request.args.get('id'))
    if id == None:
        abort(400, 'Insuffient ID specified.')
    customer = CustomerAccount.query.get(id)
    if customer != None:
        return json.dumps(customer.__dict__)
    abort(400, "This ID was not found.")

@app.route("/api/CustomerAccount/OpenCustomerAccount", methods = ["POST"])
def openAccount():
    # extract first and last name
    first_name = request.json['firstName']
    last_name = request.json['lastName']

    # first and last name validation
    if (not isinstance(first_name, str)) or (not isinstance(last_name, str)):
        abort(400, "First name or Last name are not strings")
    if (not first_name.isalpha()) or (not last_name.isalpha()):
        abort(400, "No spaces allowed in first or last name")

    # save the account
    customer_account = CustomerAccount(
        id = 0,
        account_number = str(uuid.uuid4().int),
        balance = 0.0,
        status = 1,
        first_name = first_name,
        last_name = last_name
    )
    db.session.add(customer_account)
    db.session.commit()

    # quering Customer Accounts to see if customer account
    # has been added to the database
    #customer_accounts = CustomerAccount.query.all()
    #for ca in customer_accounts:
        #print(ca.first_name)
    return ""

@app.route("/api/CustomerAccount/CloseCustomerAccount", methods = ["POST"])
def closeAccount():
    account_number = int(request.json['account_number'])
    customer_account = CustomerAccount.query.filter_by(account_number=account_number).first_or_404(description="Specified user not found")
    customer_account.status = 0
    db.session.commit()
    return json.dumps(customer_account.__dict__)

@app.route("/api/CustomerAccount/ApplyTransactionToCustomerAccount", methods = ["GET"])
def applyTransaction():
    if 'accountNumber' not in request.json or not request.json['accountNumber'].isnumeric():
        abort(400, 'Invalid account number')
    if 'amount' not in request.json or not request.json['amount'].isnumeric():
        abort(400, 'Invalid amount')
    if 'transactionType' not in request.json or (request.json['transactionType'] != '1' and request.json['transactionType'] != '2'):
        abort(400, 'Invalid transaction type')

    acc_number = int(request.json['accountNumber'])
    amount = float(request.json['amount'])
    trans_type = int(request.json['transactionType'])

    t = Transaction(uuid.uuid4().int, amount, trans_type, acc_number)
    db.session.add(t)

    cust_acc = CustomerAccount.query.filter_by(account_number=acc_number).first_or_404(description="Specified user not found")
    cust_acc.balance += amount
    db.session.commit()

    return ''

if __name__ == "__main__":
    # upon restarting application, reset the DB
    #db.drop_all()
    db.create_all()
    app.run(host="0.0.0.0")
