from TTS.api import TTS

# Modelo multilingüe XTTS
model_name = "tts_models/es/css10/vits"
tts = TTS(model_name)  # gpu=True o tts.to("cuda")
tts.to("cuda")
text = """Apolo 11 fue la misión espacial de la NASA que llevó al primer ser humano a la Luna. Su objetivo principal era lograr un aterrizaje lunar tripulado y regresar a la Tierra de manera segura.
Fecha de lanzamiento: dieciseis de julio de mil novecientos sesenta y nueve

Lugar de lanzamiento: Centro Espacial Kennedy, Florida, EE. UU.

Agencia: NASA (Estados Unidos)

Duración de la misión: 8 días, 3 horas, 18 minutos, 35 segundos
"""
output_file = "output.mp3"

tts.tts_to_file(
    text=text,
    file_path=output_file,
)

print(f" Audio guardado en {output_file}")
