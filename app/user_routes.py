from flask import Blueprint, request, jsonify
from app.models import User
from app import db

user_blueprint = Blueprint('user_blueprint', __name__)

@user_blueprint.route('/getuser', methods=['GET'])
def get_user():
    username = request.args.get('username')
    password = request.args.get('password')
    
    if not username or not password:
        return jsonify({"error": "Missing username or password"}), 400
    
    user = User.query.filter_by(username=username, password=password).first()
    
    if user:
        return jsonify({"id": user.id, "username": user.username, "password": user.password}), 200
    else:
        return jsonify({"error": "User not found"}), 404

@user_blueprint.route('/insertuser', methods=['POST'])
def insert_user():
    data = request.get_json()
    username = data.get('username')
    password = data.get('password')

    if not username or not password:
        return jsonify({"error": "Missing username or password"}), 400
    
    new_user = User(username=username, password=password)
    db.session.add(new_user)
    db.session.commit()
    
    return jsonify({"message": "User inserted successfully"}), 201
