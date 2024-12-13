from flask import Blueprint
from flask import jsonify
from flask import request

from packages import Customer
from packages import Professional
from app.admin import *

api_blueprint = Blueprint('api', __name__)

@api_blueprint.route('/')
@require_api_key
def index():
    return jsonify({'Access successful': 'Wellcome!'})

@api_blueprint.route('/add-customer', methods=['POST'])
@require_api_key
def add_customer_api():
    data = request.get_json()
    name = data.get('name')
    phone = data.get('phone')
    if name and phone is not None:
        cl = Customer(name=name, phone=phone, db_path='database/persons.db')
        cl.create_customer_table()
        return cl.add_customer()
    return jsonify({'error': 'value cannot be none'}), 400

@api_blueprint.route('/get-customers', methods=['GET'])
@require_api_key
def get_customers_api():
    cl = Customer(db_path='database/persons.db')
    return cl.get_customers(), 200

@api_blueprint.route('/add-professional', methods=['POST'])
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

@api_blueprint.route('/add-times-professional', methods=['POST'])
@require_api_key
def add_times_api():
    data = request.get_json()
    id_ = data.get('id')
    times = data.get('times')
    if id_ and times is not None:
        if isinstance(id_, int) and isinstance(times, list):
            pf = Professional(db_path='database/persons.db')
            return pf.add_times_professionals(id_, times)
        return jsonify({'error': 'check if values are "int" and "list" types '}), 400
    return jsonify({'error': 'value cannot be none'}), 400

@api_blueprint.route('/get-professionals', methods=['GET'])
@require_api_key
def get_professionals_api():
    pf = Professional(db_path='database/persons.db')
    return pf.get_professionals(), 200

@api_blueprint.route('/appointment')
@require_api_key
def appointment_api():
    data = request.get_json()
    user_id = data.get('id')
    return

@api_blueprint.route('/cancel-appointment')
@require_api_key
def cancel_appointment():
    data = request.get_json()
    user_id = data.get('id')
    return

if __name__ == '__main__':
    api_blueprint.run(debug=True)