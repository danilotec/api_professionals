from flask import Blueprint, jsonify, request
from dotenv import load_dotenv
import os

from app.models import *

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


if __name__ == '__main__':
    api_blueprint.run(debug=True)