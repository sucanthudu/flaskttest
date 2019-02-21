from app import app
from db import db

db.init_app(app)

@app.before_first_request
def create_tables():                      #create db and create_tables with columns
    db.create_all()
