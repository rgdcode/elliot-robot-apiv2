from app.speaker import generar_audio

texto = "Hola, soy Eliot. Estoy aquí para escucharte con atención."
archivo_generado = generar_audio(texto)

print(f"🟢 Archivo generado: {archivo_generado}")
