#server module
from flask import Flask
from flask_restful import Api
from flask_jwt import JWT

from security import authenticate, identity
from resources.user import UserRegister
from resources.item import Item, Itemlist
from resources.store import Store, StoreList

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///data.db'   #dblink to create
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False    #modification tracker(flask tracker off)
app.secret_key = 'kanny'                                #key for creating authentication
api = Api(app)                                          #wrap

# @app.before_first_request
# def create_tables():                                  #create db and create_tables with columns
#     db.create_all()

jwt = JWT(app, authenticate, identity)    #/auth

api.add_resource(Store,'/store/<string:name>')
api.add_resource(Item,'/item/<string:name>')
api.add_resource(Itemlist,'/items')
api.add_resource(StoreList,'/stores')
api.add_resource(UserRegister,'/register')

if __name__ == '__main__':
    from db import db
    db.init_app(app)                      #db initialized primarily(instructing sqlalchemy to take care of all)
    app.run(port=5000, debug=True)
