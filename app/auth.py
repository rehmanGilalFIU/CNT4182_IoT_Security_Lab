from functools import wraps
from flask import Blueprint, request, session, jsonify
from .database import db
bp = Blueprint('auth', __name__, url_prefix='/auth')

def logged_in(fn):
    @wraps(fn)
    def wrapper(*args, **kwargs):
        if not session.get('user_id'):
            return jsonify(error='login required'), 401
        return fn(*args, **kwargs)
    return wrapper

@bp.post('/login')
def login():
    data = request.get_json(silent=True) or {}
    username = data.get('username','')
    password = data.get('password','')
    with db() as conn:
        user = conn.execute('SELECT * FROM users WHERE username=? AND password=?', (username,password)).fetchone()
    if not user: return jsonify(error='invalid credentials'), 401
    session['user_id'] = user['id']
    session['username'] = user['username']
    session['role'] = user['role']
    return jsonify(message='logged in',role=user['role'])

@bp.post('/logout')
def logout():
    session.clear()
    return jsonify(message='logged out')

@bp.post('/change-password')
@logged_in
def change_password():
    data = request.get_json(silent=True) or {}
    new_password = data.get('new_password','')
    if len(new_password) < 4: return jsonify(error='too short'),400
    with db() as conn:
        conn.execute('UPDATE users SET password=? WHERE id=?',(new_password,session['user_id']))
    return jsonify(message='password changed')
