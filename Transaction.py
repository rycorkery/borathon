from app import get_app_db

_, db = get_app_db()

class Transaction(db.Model):
    __tablename__ = "transactions"

    id = db.Column(db.Integer, primary_key=True)
    account = db.Column(db.Integer)
    type = db.Column(db.Integer)
    associated_account = db.Column(db.Integer)

    def __init__(self, id, amount, type, associated_account):
        self.id = id
        self.amount = amount
        self.type = type
        self.associated_account = associated_account
