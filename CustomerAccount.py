from app import get_app_db

_, db = get_app_db()

class CustomerAccount(db.Model):
    __tablename__ = "customer_account"

    id = db.Column(db.BigInteger, primary_key=True)
    account_number = db.Column(db.String(128))
    balance = db.Column(db.Numeric)
    status = db.Column(db.Integer)
    first_name = db.Column(db.String(64))
    last_name = db.Column(db.String(64))

    def __str__(self):
        return f"{self.id} | {self.account_number} | {self.balance} | {self.status} | {self.first_name} | {self.last_name}"

    def __init__(self, id, account_number, balance, status, first_name, last_name):
        self.id = id
        self.account_number = account_number
        self.balance = balance
        self.status = status
        self.first_name = first_name
        self.last_name = last_name
