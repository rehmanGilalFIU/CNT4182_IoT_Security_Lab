import os
import subprocess
from flask import Blueprint,request,jsonify,session
from .auth import logged_in
from .database import db
bp=Blueprint('admin',__name__,url_prefix='/api/admin')

@bp.get('/users')
@logged_in
def users():
    if session.get('role') != 'admin': return jsonify(error='forbidden'),403
    with db() as conn:
        rows=conn.execute('SELECT id,username,role,email FROM users').fetchall()
    return jsonify([dict(r) for r in rows])

@bp.post('/promote')
@logged_in
def promote():
    data=request.get_json(silent=True) or {}
    target=data.get('user_id')
    role=data.get('role','resident')
    with db() as conn:
        conn.execute('UPDATE users SET role=? WHERE id=?',(role,target))
    return jsonify(message='updated')

@bp.get('/diagnostics')
@logged_in
def diagnostics():
    host=request.args.get('host','127.0.0.1')
    # Lab mode: do not actually execute shell commands. Demonstrates unsafe construction.
    command = 'ping -c 1 ' + host
    return jsonify(planned_command=command,warning='simulation only')

@bp.get('/config')
@logged_in
def config():
    return jsonify(debug=os.getenv('FLASK_DEBUG','0'),environment=dict(os.environ))
