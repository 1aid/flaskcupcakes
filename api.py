from flask import jsonify, request
from models import db, Cupcake
from app import app

@app.route('/api/cupcakes', methods=['GET'])
def get_cupcakes():
    cupcakes = Cupcake.query.all()
    return jsonify(cupcakes=[cupcake.serialize() for cupcake in cupcakes])

@app.route('/api/cupcakes/<int:cupcake_id>', methods=['GET'])
def get_cupcake(cupcake_id):
    cupcake = Cupcake.query.get_or_404(cupcake_id)
    return jsonify(cupcake.serialize())

@app.route('/api/cupcakes', methods=['POST'])
def create_cupcake():
    data = request.json
    cupcake = Cupcake(**data)
    db.session.add(cupcake)
    db.session.commit()
    return jsonify(cupcake.serialize()), 201

@app.route('/api/cupcakes/<int:cupcake_id>', methods=['PATCH'])
def update_cupcake(cupcake_id):
    cupcake = Cupcake.query.get_or_404(cupcake_id)
    data = request.json
    for key, value in data.items():
        setattr(cupcake, key, value)
    db.session.commit()
    return jsonify(cupcake.serialize())

@app.route('/api/cupcakes/<int:cupcake_id>', methods=['DELETE'])
def delete_cupcake(cupcake_id):
    cupcake = Cupcake.query.get_or_404(cupcake_id)
    db.session.delete(cupcake)
    db.session.commit()
    return jsonify(message='Deleted')