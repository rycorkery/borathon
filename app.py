from flask_sqlalchemy import SQLAlchemy
from flask import Flask

# Connect to the database
ENDPOINT = "corkeryr-db.cfbtwcgfvkzx.us-east-1.rds.amazonaws.com"
PORT = "3306"
USER = "admin"
PASSWORD = "test1234!!?"
REGION = "us-east-1"
DBNAME = "borathon"
connect_string = 'mysql+pymysql://{}:{}@{}:{}/{}?charset=utf8mb4'.format(USER, PASSWORD, ENDPOINT, PORT, DBNAME)
# connect_string = f"mysql://{USER}:{PASSWORD}@{ENDPOINT}:{PORT}/{DBNAME}"
# connection = create_engine(connect_string, echo = True)

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = connect_string
db = SQLAlchemy(app)

def get_app_db():
    return app, db