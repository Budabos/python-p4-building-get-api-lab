#!/usr/bin/env python3

from flask import Flask, make_response, jsonify
from flask_migrate import Migrate
from models import db, Bakery, BakedGood

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///app.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.json.compact = False

migrate = Migrate(app, db)
db.init_app(app)

@app.route('/')
def index():
    return '<h1>Bakery GET API</h1>'

@app.route('/bakeries')
def get_bakeries():
    with app.app_context():
        bakeries_list = Bakery.query.all()
        return jsonify([bakery.to_dict() for bakery in bakeries_list])

@app.route('/bakeries/<int:id>')
def get_bakery_by_id(id):
    with app.app_context():
        bakery = Bakery.query.get(id)
        if bakery:
            return jsonify(bakery.to_dict())
        else:
            return make_response(jsonify({'error': 'Bakery not found'}), 404)

@app.route('/baked_goods/by_price')
def get_baked_goods_by_price():
    with app.app_context():
        goods_by_price = BakedGood.query.order_by(BakedGood.price.desc()).all()
        return jsonify([good.to_dict() for good in goods_by_price])

@app.route('/baked_goods/most_expensive')
def get_most_expensive_baked_good():
    with app.app_context():
        most_exp_good = BakedGood.query.order_by(BakedGood.price.desc()).first()
        if most_exp_good:
            return jsonify(most_exp_good.to_dict())
        else:
            return make_response(jsonify({'error': 'No baked goods found'}), 404)

if __name__ == '__main__':
    app.run(port=5555, debug=True)
