from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import MetaData
from sqlalchemy_serializer import SerializerMixin

metadata = MetaData(naming_convention={
    "fk": "fk_%(table_name)s_%(column_0_name)s_%(referred_table_name)s",
})

db = SQLAlchemy(metadata=metadata)

class Bakery(db.Model, SerializerMixin):
    __tablename__ = 'bakeries'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50),nullable=False)
    created_at = db.Column(db.DateTime,nullable= False)
    updated_at = db.Column(db.DateTime,nullable= False)
    baked_goods =db.relationship('BakedGood',backref='bakeries')

def __repr__(self):
    return f'<Bakery "{self.name}">'

class BakedGood(db.Model, SerializerMixin):
    __tablename__ = 'baked_goods'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(255), nullable=False)
    price = db.Column(db.Integer,nullable=False)
    bakery_id = db.Column (db.Integer,db.ForeignKey('bakeries.id'))
    created_at = db.Column(db.DateTime,nullable=False)
    updated_at = db.Column(db.DateTime,nullable=False)

def __repr__(self):
    return f'<BakedGood "{self.name}">'