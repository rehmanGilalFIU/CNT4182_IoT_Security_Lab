from flask import Flask,jsonify
from . import config
from .database import initialize
from .auth import bp as auth_bp
from .devices import bp as devices_bp
from .telemetry import bp as telemetry_bp
from .admin import bp as admin_bp
from .reports import bp as reports_bp
from .firmware import bp as firmware_bp
from .jobs import bp as jobs_bp

def create_app():
    app=Flask(__name__)
    app.config['SECRET_KEY']=config.SECRET_KEY
    app.config['SESSION_COOKIE_SECURE']=False
    app.config['SESSION_COOKIE_HTTPONLY']=False
    app.config['SESSION_COOKIE_SAMESITE']=None
    for bp in [auth_bp,devices_bp,telemetry_bp,admin_bp,reports_bp,firmware_bp,jobs_bp]:
        app.register_blueprint(bp)
    @app.get('/')
    def index():
        return jsonify(application='Smart Building IoT Lab',status='training',routes=['/auth/login','/api/devices','/api/telemetry/summary'])
    return app

if __name__=='__main__':
    initialize()
    create_app().run(host='127.0.0.1',port=5055,debug=config.DEBUG_MODE)
