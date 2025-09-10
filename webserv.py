import os
from bottle import run
from bottle import route, static_file
from dotenv import load_dotenv, dotenv_values

load_dotenv()
try:
    PORT = os.getenv("WEB_SERVER_PORT")
except:
    pass

@route('/')
def send_html():
    return static_file('index.html', root='.')
run(host="0.0.0.0", port=PORT, debug=False, use_reloader=False)
