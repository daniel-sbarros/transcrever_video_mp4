# pip install mysql-connector-python flask-sqlalchemy flask==3.0.2 flask-wtf==1.0.0 flask-bcrypt werkzeug==2.2.3
# instalar openai-whisper: pip install openai-whisper ~> https://github.com/openai/whisper
# instalar ffmpeg: https://www.geeksforgeeks.org/how-to-install-ffmpeg-on-windows/
# Importar a biblioteca pydub
from flask import Flask

app = Flask(__name__)
app.config.from_pyfile('config.py')

from app.views.views import *

if __name__ == "__main__":
    app.run(debug=True)
