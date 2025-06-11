import openai
import os 



openai.api_key = os.getenv("openai_api_key")

def generar_respuesta_emocional(texto_usuario):
    prompt = f"Eres un asistente emocional. Responde con empatía a: \"{texto_usuario}\""
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[{"role": "user", "content": prompt}]
    )
    return response.choices[0].message.content