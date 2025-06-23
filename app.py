from flask import Flask, request, jsonify
from nltk.sentiment.vader import SentimentIntensityAnalyzer
import nltk
from mensajes import generar_respuesta
from perfil import actualizar_perfil, obtener_perfil

nltk.download('vader_lexicon')

app = Flask(__name__)
analyzer = SentimentIntensityAnalyzer()
perfil_usuario = []

@app.route("/analizar", methods=["POST"])
def analizar():
    data = request.get_json()
    texto = data.get("texto", "")

    scores = analyzer.polarity_scores(texto)
    comp = scores['compound']

    if comp >= 0.1:
        emocion = "POSITIVO"
    elif comp <= -0.1:
        emocion = "NEGATIVO"
    else:
        emocion = "NEUTRAL"

    # Generar recomendación
    mensaje, recomendacion = generar_respuesta(emocion, texto)

    # Guardar para perfil
    perfil_usuario.append((texto, emocion))
    perfil = actualizar_perfil(perfil_usuario)

    return jsonify({
        "emocion": emocion,
        "mensaje": mensaje,
        "recomendacion": recomendacion,
        "perfil_actual": perfil
    })

@app.route("/perfil", methods=["GET"])
def perfil():
    return jsonify(obtener_perfil(perfil_usuario))

if __name__ == "__main__":
    app.run()
