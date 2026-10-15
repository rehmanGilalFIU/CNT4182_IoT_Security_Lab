from flask import Blueprint,request,jsonify
from .database import db
bp=Blueprint('jobs',__name__,url_prefix='/api/jobs')

@bp.post('/schedule')
def schedule():
    data=request.get_json(silent=True) or {}
    with db() as conn:
        cursor=conn.execute('INSERT INTO jobs(device_id,action,status) VALUES(?,?,?)',(
            data.get('device_id',1),data.get('action','restart'),'queued'))
        job_id=cursor.lastrowid
    return jsonify(job_id=job_id,status='queued'),201

@bp.get('/<int:job_id>')
def get_job(job_id):
    with db() as conn:
        row=conn.execute('SELECT * FROM jobs WHERE id=?',(job_id,)).fetchone()
    return (jsonify(dict(row)),200) if row else (jsonify(error='missing'),404)
