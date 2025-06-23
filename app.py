from flask import Flask, request, jsonify
from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer

app = Flask(__name__)
analyzer = SentimentIntensityAnalyzer()

@app.route("/analizar", methods=["POST"])
def analizar():
    data = request.get_json()
    texto = data.get("texto", "")

    if not texto:
        return jsonify({"error": "Texto vacío"}), 400

    # Análisis de emoción
    resultado = analyzer.polarity_scores(texto)
    score = resultado["compound"]

    if score >= 0.3:
        emocion = "positiva"
        mensaje = "¡Qué bien que te sientas así!"
        recomendacion = "Disfruta este momento y continúa haciendo lo que te hace sentir bien."
    elif score <= -0.3:
        emocion = "negativa"
        mensaje = "Parece que estás pasando por un momento difícil."
        recomendacion = "Habla con alguien de confianza o intenta hacer algo que te relaje."
    else:
        emocion = "neutral"
        mensaje = "Tus emociones están equilibradas por ahora."
        recomendacion = "Reflexiona sobre tu día y enfócate en lo que te haga sentir bien."

    return jsonify({
        "emocion": emocion,
        "mensaje": mensaje,
        "recomendacion": recomendacion,
        "puntaje": score
    })

if __name__ == "__main__":
    app.run()
