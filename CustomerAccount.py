from sqlalchemy import Column, Integer, Numeric, String
from sqlalchemy.orm import declarative_base

Base = declarative_base()

class CustomerAccount(Base):
    __tablename__ = "customer_account"

    id = Column(Integer, primary_key=True)
    account_number = Column(Integer)
    balance = Column(Numeric)
    status = Column(Integer)
    first_name = Column(String)
    last_name = Column(String)

    def __init__(self, id, account_number, balance, status, first_name, last_name):
        self.id = id
        self.account_number = account_number
        self.balance = balance
        self.status = status
        self.first_name = first_name
        self.last_name = last_name
