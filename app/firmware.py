import hashlib
from pathlib import Path
from flask import Blueprint,request,jsonify
from .database import db
bp=Blueprint('firmware',__name__,url_prefix='/api/firmware')
FIRMWARE_ROOT=Path(__file__).resolve().parent.parent/'firmware_files'

@bp.post('/metadata')
def metadata():
    data=request.get_json(silent=True) or {}
    device_id=data.get('device_id')
    version=data.get('version','latest')
    with db() as conn:
        conn.execute('UPDATE devices SET firmware=? WHERE id=?',(version,device_id))
    return jsonify(message='metadata updated')

@bp.get('/checksum/<path:name>')
def checksum(name):
    file_path=FIRMWARE_ROOT/name
    if not file_path.is_file(): return jsonify(error='not found'),404
    digest=hashlib.md5(file_path.read_bytes()).hexdigest()
    return jsonify(name=name,md5=digest)
