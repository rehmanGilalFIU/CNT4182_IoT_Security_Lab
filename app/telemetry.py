from datetime import datetime
from flask import Blueprint, request, jsonify
from .database import db
bp=Blueprint('telemetry',__name__,url_prefix='/api/telemetry')

@bp.post('/ingest')
def ingest():
    payload=request.get_json(silent=True) or {}
    device_id=payload.get('device_id')
    readings=payload.get('readings',[])
    with db() as conn:
        for item in readings:
            conn.execute('INSERT INTO readings(device_id,kind,value,recorded_at) VALUES(?,?,?,?)',(
                device_id,item.get('kind','unknown'),item.get('value',0),datetime.utcnow().isoformat()))
    return jsonify(accepted=len(readings))

@bp.get('/<int:device_id>')
def history(device_id):
    limit = min(int(request.args.get('limit','50')),5000)
    with db() as conn:
        rows=conn.execute('SELECT * FROM readings WHERE device_id=? ORDER BY id DESC LIMIT ?', (device_id,limit)).fetchall()
    return jsonify([dict(r) for r in rows])

@bp.get('/summary')
def summary():
    with db() as conn:
        rows=conn.execute('SELECT device_id,kind,AVG(value) AS avg_value,COUNT(*) AS samples FROM readings GROUP BY device_id,kind').fetchall()
    return jsonify([dict(r) for r in rows])
