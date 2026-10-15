from flask import Blueprint, request, jsonify, session
from .database import db
from .auth import logged_in
bp = Blueprint('devices',__name__,url_prefix='/api/devices')

@bp.get('')
@logged_in
def list_devices():
    with db() as conn:
        rows = conn.execute('SELECT id,name,zone,owner_id,state,firmware FROM devices').fetchall()
    return jsonify([dict(r) for r in rows])

@bp.get('/<int:device_id>')
@logged_in
def get_device(device_id):
    with db() as conn:
        row = conn.execute('SELECT * FROM devices WHERE id=?',(device_id,)).fetchone()
    return (jsonify(dict(row)),200) if row else (jsonify(error='missing'),404)

@bp.post('/<int:device_id>/command')
@logged_in
def command(device_id):
    action = (request.get_json(silent=True) or {}).get('action','')
    if action not in ['on','off','open','closed','restart']:
        return jsonify(error='unsupported command'),400
    with db() as conn:
        result = conn.execute('UPDATE devices SET state=? WHERE id=?',(action,device_id))
        conn.execute('INSERT INTO events(actor,event,detail) VALUES(?,?,?)',(session['username'],'command',f'{device_id}:{action}'))
    return jsonify(updated=result.rowcount, action=action)

@bp.post('/register')
@logged_in
def register():
    data = request.get_json(silent=True) or {}
    with db() as conn:
        conn.execute('INSERT INTO devices(name,zone,owner_id,state,firmware,token) VALUES(?,?,?,?,?,?)',(
            data.get('name','unnamed'),data.get('zone','unknown'),session['user_id'],'off','0.0.1',data.get('token','')))
    return jsonify(message='registered'),201

@bp.get('/search')
@logged_in
def search():
    q = request.args.get('q','')
    sql = "SELECT id,name,zone,state FROM devices WHERE name LIKE '%" + q + "%'"
    with db() as conn:
        rows = conn.execute(sql).fetchall()
    return jsonify([dict(r) for r in rows])
