from flask import Blueprint, jsonify, request
from dotenv import load_dotenv
from packages import Customer, Professional
import os

from app.main import *

api_blueprint = Blueprint('api', __name__)

load_dotenv()

API_KEY = os.getenv('API_KEY')

def require_api_key(func):
    def wrapper(*args, **kwargs):
        api_key_aut = request.headers.get('X-API-KEY')
        if not api_key_aut or api_key_aut != API_KEY:
            return jsonify({'error': 'Access denied'}), 401
        return func(*args, **kwargs)
    wrapper.__name__ = func.__name__
    return wrapper

@api_blueprint.route('/')
@require_api_key
def index():
    return jsonify({'Access successful': 'Wellcome!'})

@api_blueprint.route('/add_customer', methods=['POST'])
@require_api_key
def add_customer_api():
    data = request.get_json()
    name = data.get('name')
    phone = data.get('phone')
    print(name)
    print(phone)
    if name and phone is not None:
        cl = Customer(name=name, phone=phone, db_path='database/persons.db')
        cl.create_customer_table()
        return cl.add_customer()
    return jsonify({'error': 'value cannot be none'}), 400

@api_blueprint.route('/get_customers', methods=['GET'])
@require_api_key
def get_customers_api():
    cl = Customer(db_path='database/persons.db')
    return cl.get_customers(), 200

@api_blueprint.route('/add_professional', methods=['POST'])
@require_api_key
def add_profesional_api():
    data = request.get_json()
    name = data.get('name')
    specialty = data.get('specialty')
    if name and specialty is not None:
        pf = Professional(name=name, specialty=specialty, db_path='database/persons.db')
        pf.create_professional_table()
        return pf.add_professional()
    return jsonify({'error': 'value cannot be none'}), 400

@api_blueprint.route('/get_professionals', methods=['GET'])
@require_api_key
def get_professionals_api():
    pf = Professional(db_path='database/persons.db')
    return pf.get_professionals(), 200

if __name__ == '__main__':
    api_blueprint.run(debug=True)