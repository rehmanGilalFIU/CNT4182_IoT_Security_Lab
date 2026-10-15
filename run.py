from app.main import create_app
from app.database import initialize
initialize()
app=create_app()
if __name__=='__main__':
    app.run(host='127.0.0.1',port=5055,debug=False)
