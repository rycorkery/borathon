class Transaction:
    def __init__(self, id, amount, type, associated_account):
        self.id = id
        self.amount = amount
        self.type = type
        self.associated_account = associated_account
