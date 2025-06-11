import boto3
from pydub import AudioSegment
import os

# 🔧 Ruta a tu instalación de ffmpeg (ajústala según tu carpeta real)
os.environ["PATH"] += os.pathsep + r"C:\ffmpeg-7.1.1-essentials_build\bin"
AudioSegment.converter = r"C:\ffmpeg-7.1.1-essentials_build\bin\ffmpeg.exe"
AudioSegment.ffprobe = r"C:\ffmpeg-7.1.1-essentials_build\bin\ffprobe.exe"

# 🔐 Credenciales AWS (usa variables de entorno en producción real)
AWS_ACCESS_KEY_ID = os.getenv("AWS_ACCESS_KEY_ID")
AWS_SECRET_ACCESS_KEY = os.getenv("AWS_SECRET_ACCESS_KEY")
AWS_REGION = os.getenv("AWS_REGION")

def generar_audio(texto, filename_wav='respuesta.wav', voz='Pedro'):
    filename_mp3 = 'temp.mp3'

    # Inicializar cliente Polly
    polly = boto3.client(
        'polly',
        aws_access_key_id=AWS_ACCESS_KEY_ID,
        aws_secret_access_key=AWS_SECRET_ACCESS_KEY,
        region_name=AWS_REGION
    )

    try:
        # Solicitar audio en formato MP3
        response = polly.synthesize_speech(
            Text=texto,
            OutputFormat='mp3',
            VoiceId=voz,
            Engine='neural'  # Cambiar a 'standard' si da error
        )

        # Guardar archivo temporal MP3
        with open(filename_mp3, 'wb') as f:
            f.write(response['AudioStream'].read())

        # Convertir a WAV
        audio = AudioSegment.from_file(filename_mp3, format='mp3')
        audio.export("audios/"+filename_wav, format='wav')

        # Eliminar temporal
        os.remove(filename_mp3)

        print(f"✅ Audio generado en WAV: {filename_wav}")
        
        return os.path.join("../audios", filename_wav) 

    except Exception as e:
        print(f"❌ Error generando audio: {e}")
        return None
