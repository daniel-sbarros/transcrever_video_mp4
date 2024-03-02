# PROJETO FLASK - TRANSCREVER ARQUIVO MP4
<p style="text-align:justify">
O obetivo do projeto é carregar um arquivo mp4 e transcrever o seu audio usando a biblioteca <span style="font-weight:bold; font-style:italic">Whisper</span> da <span style="font-weight:bold; font-style:italic">OpenAI</span> (<span style="font-style:italic">openai-whisper</span>).
</p>
<p style="text-align:justify">
Primeiro o vídeo é carregado na página inicial e salvo na pasta /temp e extraimos o audio dele com a biblioteca <span style="font-weight:bold; font-style:italic">pydub</span> e o salvamos na pasta <span style="font-weight:bold; font-style:italic">/temp</span>, então, no audio criado utilizamos a biblioteca whisper para transcrever o audio e imprimimos o resultado na pagina <span style="font-weight:bold; font-style:italic">/transcricao</span>, e deletamos os arquivos de audio e video carregados e criados no processo.
</p>
<p style="text-align:justify; color:red; font-style:italic">
Obs.: Essa versão de teste está usando o Model <span style="font-weight:bold; font-style:italic">tiny</span> da biblioteca Whisper, para melhores resultados na transcrição eu indico usar o Model <span style="font-weight:bold; font-style:italic">large</span>, porém ele ocupa muito mais espaço em disco, quase 3 gb, e o seu processo de transcrição é muito mais lento.</p>

## BIBLIOTECAS USADAS
- [Flask Framework](https://flask.palletsprojects.com/en/3.0.x/)
- [Openai Whisper](https://github.com/openai/whisper)
- ffmpeg
- PyDub

## PASSO A PASSO
1. INSTALE O ffmpeg SEGUINDO O PASSO-A-PASSO ENCONTRADO NESTE LINK: [Tutorial de Instalação ffmpeg](https://www.geeksforgeeks.org/how-to-install-ffmpeg-on-windows/).
2. CRIE O ARQUIVO ***config.py*** NA RAIZ DO SISTEMA COM O CONTEÚDO ABAIXO:
```python
import os


SECRET_KEY = 'sua_key'
TEMP_PATH = os.path.dirname(os.path.abspath(__file__)) + '/temp'
MODEL = 'tiny'  # opções de modelos: tiny, base, small, medium, large
```
3. INSTALE AS BIBLIOTECAS A PARTIR DO ARQUIVO ***requeriments.txt*** COM O COMANDO ABAIXO:
```sh
pip install -r requeriments.txt
```
