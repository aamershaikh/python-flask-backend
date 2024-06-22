from flask import Blueprint, request, jsonify
from flask_jwt_extended import jwt_required
from app.models import User
from app import db

account_blueprint = Blueprint('account_blueprint', __name__)

@account_blueprint.route('/getaccount', methods=['GET'])
@jwt_required()
def get_account():
        return jsonify({"message": "accountfound"}), 201 