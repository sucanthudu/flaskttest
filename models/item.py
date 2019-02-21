import sqlite3
from db import db

class ItemModel(db.Model):
    __tablename__='items'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80))
    price = db.Column(db.Float(precision=2))

    store_id = db.Column(db.Integer, db.ForeignKey('stores.id'))    #using this we can find out which store this item belong to
    store = db.relationship('StoreModel')

    def __init__(self, name, price, store_id):
        self.name = name
        self.price = price
        self.store_id = store_id

    def json(self):
        return {'name':self.name,'price':self.price,'available_in_store_id':self.store_id}

    @classmethod
    def find_by_name(cls, name):
        return cls.query.filter_by(name=name).first()        #select * from items where name=name first match row

    def save_to_db(self):
        db.session.add(self)       #session is collection of objects
        db.session.commit()

    def delete_to_db(self):
        db.session.delete(self)
        db.session.commit()
