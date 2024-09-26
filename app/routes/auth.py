from flask import Blueprint, request, jsonify
from app.services.auth_service import authenticate

auth_bp = Blueprint('auth', __name__)

@auth_bp.route('/signin', methods=['POST'])
def signin():
    data = request.get_json()
    email = data.get('email')
    password = data.get('password')

    access_token = authenticate(email, password)
    
    if access_token:
        return jsonify({"access_token": access_token}), 200
    return jsonify({'message': 'you are not authenticated'}), 401
