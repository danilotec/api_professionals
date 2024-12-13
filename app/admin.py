from dotenv import load_dotenv
from flask import jsonify
from flask import request
import os

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