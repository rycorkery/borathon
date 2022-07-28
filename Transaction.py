from sqlalchemy import Column, Integer, Numeric
from sqlalchemy.orm import declarative_base

Base = declarative_base()

class Transaction(Base):
    __tablename__ = "transactions"

    id = Column(Integer, primary_key=True)
    account = Column(Integer)
    type = Column(Integer)
    associated_account = Column(Integer)

    def __init__(self, id, amount, type, associated_account):
        self.id = id
        self.amount = amount
        self.type = type
        self.associated_account = associated_account
