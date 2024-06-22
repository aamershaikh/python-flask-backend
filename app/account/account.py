from flask import Blueprint, request, jsonify
from flask_jwt_extended import jwt_required
from app.models import Account
from app import db

account_blueprint = Blueprint('account_blueprint', __name__)

@account_blueprint.route('/getaccount', methods=['GET'])
@jwt_required()
def get_account():
    account_number = request.args.get('account_number')
    
    if not account_number:
        return jsonify({"error": "Missing account number"}), 400
    
    account = Account.query.filter_by(account_number=account_number).first()
    
    if account:
        return jsonify({
            "id": account.id,
            "account_number": account.account_number,
            "summarizatioavailable": account.summarizatioavailable,
            "accountsummary": account.accountsummary,
            "summarytext": account.summarytext
        }), 200
    else:
        return jsonify({"error": "Account not found"}), 404 