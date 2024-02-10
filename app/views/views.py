# importar app de run.py
import os
from flask import flash, redirect, render_template, request, url_for
from app.helpers.helpers import convert_mp4_to_mp3, transcribe_mp3
from run import app

@app.route('/')
def index():
    return render_template('index.html', title='Transcrever Video MP4')

@app.route('/transcrever', methods=['POST'])
def transcrever():
    arquivo = request.files['arquivo']
    
    if not arquivo.filename.endswith('.mp4'):
        flash('Arquivo invalido')
        return redirect(url_for('index'))
    
    video_path = os.path.join(app.config['TEMP_PATH'], arquivo.filename)
    arquivo.save(video_path)
    audio_path = convert_mp4_to_mp3(video_path)
    if not audio_path:
        flash('Nao foi possivel converter o arquivo para MP3.')
        return redirect(url_for('index'))

    transcricao = transcribe_mp3(audio_path, 'tiny')
    if not transcricao:
        flash('Não foi possivel transcrever o arquivo.')
        return redirect(url_for('index'))
    
    os.remove(audio_path) if os.path.exists(audio_path) else None
    os.remove(video_path) if os.path.exists(video_path) else None

    return render_template('transcricao.html', title=f'Transcição do video "{arquivo.filename}"', transcricao=transcricao)

