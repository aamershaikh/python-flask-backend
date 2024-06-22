from flask import Blueprint, request, jsonify
from werkzeug.security import generate_password_hash, check_password_hash
from flask_jwt_extended import create_access_token
from app.models import User
from app import db

user_blueprint = Blueprint('user_blueprint', __name__)

@user_blueprint.route('/login', methods=['GET'])
def get_user():
    username = request.args.get('username')
    password = request.args.get('password')
    
    if not username or not password:
        return jsonify({"error": "Missing username or password"}), 400
    
    user = User.query.filter_by(username=username).first()
    
    if user and check_password_hash(user.password, password):
        access_token = create_access_token(identity=username)
        return jsonify({"id": user.id, "username": user.username, "access_token":access_token}), 200
    else:
        return jsonify({"error": "User not found or password incorrect"}), 404

@user_blueprint.route('/register', methods=['POST'])
def insert_user():
    data = request.get_json()
    username = data.get('username')
    password = data.get('password')

    if not username or not password:
        return jsonify({"error": "Missing username or password"}), 400
    
    hashed_password = generate_password_hash(password, method='sha256')
    new_user = User(username=username, password=hashed_password)
    db.session.add(new_user)
    db.session.commit()
    
    return jsonify({"message": "User inserted successfully"}), 201
