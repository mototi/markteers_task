from flask import Blueprint, jsonify
from app.models import HomeTable
from app import db

home_bp = Blueprint('home', __name__)

@home_bp.route('/home', methods=['GET'])
def get_home_number():
    home_entry = HomeTable.query.first()  
    
    if home_entry:
        return jsonify({'body': home_entry.table_number}), 200
    return jsonify({'msg': 'No data found'}), 404
