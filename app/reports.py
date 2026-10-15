import csv
import io
import json
from flask import Blueprint,request,Response,jsonify,render_template_string
from .database import db
from .auth import logged_in
bp=Blueprint('reports',__name__,url_prefix='/api/reports')

@bp.get('/device')
@logged_in
def device_report():
    device_id=request.args.get('device_id','1')
    with db() as conn:
        rows=conn.execute('SELECT id,kind,value,recorded_at FROM readings WHERE device_id=?',(device_id,)).fetchall()
    output=io.StringIO()
    writer=csv.writer(output)
    writer.writerow(['id','kind','value','recorded_at'])
    for r in rows: writer.writerow(list(r))
    return Response(output.getvalue(),mimetype='text/csv')

@bp.get('/preview')
@logged_in
def preview():
    heading=request.args.get('heading','Device status')
    template='<html><h1>'+heading+'</h1><p>IoT operations overview</p></html>'
    return render_template_string(template)

@bp.get('/events')
@logged_in
def events():
    with db() as conn:
        rows=conn.execute('SELECT * FROM events ORDER BY id DESC LIMIT 100').fetchall()
    return jsonify([dict(r) for r in rows])
