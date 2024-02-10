from pydub import AudioSegment  # Importar a biblioteca pydub
import whisper  # Importar a biblioteca openai-whisper

def convert_mp4_to_mp3(file_path: str):
    if file_path.endswith('.mp4'):
        audio = AudioSegment.from_file(file_path, format="mp4")  # Abrir o arquivo mp4 como um segmento de áudio
        mp3_path = f"{file_path.replace('.mp4', '')}.mp3"
        audio.export(mp3_path, format="mp3")  # Exportar o segmento de áudio como um arquivo mp3
        print(f'Arquivo {file_path} convertido para {mp3_path}.')

        return mp3_path
    else:
        return None
    

def formata_seg(segundos):
    horas = segundos // 3600
    minutos = (segundos % 3600) // 60
    segundos = (segundos % 3600) % 60

    return "{:02d}:{:02d}:{:02d}".format(horas, minutos, segundos)

def transcribe_mp3(audio_path, modelo):
    try:
        model = whisper.load_model(modelo)
        result = model.transcribe(audio_path)
        texto_com_tempo = []
        
        print('Iniciado transcricão. Aguarde...')
        for segment in result['segments']:
            s_time = formata_seg(round(float(segment['start'])))
            s_text = segment['text']

            texto_com_tempo.append(f'[{s_time}]\t{s_text}')

        texto_completo = result['text'].replace('. ', '.\n').replace('? ', '?\n').split('\n')

        print('Tarefa executada com sucesso.')
        return { 'texto_completo': texto_completo, 'texto_com_tempo': texto_com_tempo }
    except Exception as err:
        print(f'Erro ao tentar transcrever o audio do arquivo. \n\n{err}')
        return None
