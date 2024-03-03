import os
import re
import time
from flask import flash, redirect, render_template, request, url_for, send_file
from app.helpers.helpers import convert_mp4_to_mp3, create_txt_file, delete_files, read_txt_file, transcribe_mp3
from run import app

@app.route('/')
def index():
    alert = request.args.get('alert')
    return render_template('index.html', title='Transcrever Video MP4', alert=alert)

@app.route('/transcrever', methods=['POST'])
def transcrever():
    delete_files()
    arquivo = request.files['arquivo']
    
    if not arquivo.filename.endswith('.mp4'):
        flash('Arquivo invalido')
        return redirect(url_for('index'))
    
    video_path = os.path.join(app.config['TEMP_PATH'], f'v{time.time()}.mp4')
    arquivo.save(video_path)
    audio_path = convert_mp4_to_mp3(video_path)
    if not audio_path:
        flash('Nao foi possivel converter o arquivo para MP3.')
        return redirect(url_for('index'))

    transcricao = transcribe_mp3(audio_path, modelo=app.config['MODEL'])
    if not transcricao:
        flash('Não foi possivel transcrever o arquivo.')
        return redirect(url_for('index'))
    
    create_txt_file('texto_completo', transcricao)
    create_txt_file('texto_com_tempo', transcricao)

    title = f'Transcição do video "{arquivo.filename}"'

    if os.path.isfile(transcricao['legend_path']):
        nome_arquivo = re.search(r'[^\\/]+$', transcricao['legend_path']).group()
        return redirect(url_for('resultado', title=title, legend_path=nome_arquivo))
    else:
        flash('Não foi possivel transcrever o arquivo.')
        return redirect(url_for('index', alert='danger'))

@app.route('/resultado')
def resultado():
    try:
        title = request.args.get('title')        
        texto_completo = read_txt_file('texto_completo')
        texto_com_tempo = read_txt_file('texto_com_tempo')
        legend_path = request.args.get('legend_path')
        
        return render_template('transcricao.html', title=title, transcricao={'texto_completo':texto_completo, 'texto_com_tempo':texto_com_tempo, 'legend_path':legend_path})
    except Exception as err:
        flash(f'Erro ao transcrever o arquivo. \n\n{err}')
        return redirect(url_for('index', alert='danger'))

@app.route('/download/<path:filename>')
def download_file(filename):
    directory = 'downloads/'
    return send_file(os.path.join(directory, filename), as_attachment=True)
