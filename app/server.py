from flask import Flask, request, send_file
import os
from app.transcriber import transcribir_audio
from app.emotional_model import generar_respuesta_emocional
from app.speaker import generar_audio

app = Flask(__name__)
UPLOAD_FOLDER = 'audios'
os.makedirs(UPLOAD_FOLDER, exist_ok=True)

@app.route('/audio', methods=['POST'])
def receive_audio():
    print("🔔 POST binario recibido")

    raw_data = request.get_data()
    if len(raw_data) < 500:
        return {'status': 'error', 'message': 'Audio vacío'}, 400

    input_path = os.path.join(UPLOAD_FOLDER, 'usuario.wav')
    output_path = os.path.join(UPLOAD_FOLDER, 'respuesta.wav')

    with open(input_path, 'wb') as f:
        f.write(raw_data)

    try:
        texto = transcribir_audio(input_path)
        respuesta = generar_respuesta_emocional(texto)

        output_path = generar_audio(respuesta)  # Genera y devuelve ruta absoluta
        print("🔄 Generando audio nuevo en:", output_path)
        return send_file(output_path, mimetype='audio/wav')


    except Exception as e:
        print(f"❗ Error: {e}")
        return {'status': 'error', 'message': str(e)}, 500
