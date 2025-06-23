# app.py
from flask import Flask, request, jsonify
from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer

app = Flask(__name__)
analyzer = SentimentIntensityAnalyzer()

entradas = []  # simulamos almacenamiento para perfil emocional

@app.route("/analizar", methods=["POST"])
def analizar():
    data = request.get_json()
    texto = data.get("texto", "")

    if not texto:
        return jsonify({"error": "Texto vacío"}), 400

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

    # Guardar entrada para perfil
    entradas.append({"texto": texto, "emocion": emocion, "score": score})

    return jsonify({
        "emocion": emocion,
        "mensaje": mensaje,
        "recomendacion": recomendacion,
        "puntaje": score
    })

@app.route("/perfil", methods=["GET"])
def perfil():
    if not entradas:
        return jsonify({
            "total_entradas": 0,
            "perfil": "No se han registrado entradas suficientes para generar un perfil."
        })

    total = len(entradas)
    positivas = sum(1 for e in entradas if e["emocion"] == "positiva")
    negativas = sum(1 for e in entradas if e["emocion"] == "negativa")
    neutrales = total - positivas - negativas

    resumen = f"Has registrado {total} entradas. De ellas, {positivas} fueron positivas, {negativas} negativas y {neutrales} neutrales."

    if positivas > negativas:
        perfil = "Tu perfil emocional es predominantemente positivo. Eres una persona con actitud optimista y resiliente."
    elif negativas > positivas:
        perfil = "Tu perfil emocional refleja momentos difíciles. Es importante cuidar tu salud mental y buscar apoyo cuando lo necesites."
    else:
        perfil = "Tu perfil emocional está equilibrado. Tienes una buena capacidad para adaptarte a distintas situaciones."

    return jsonify({
        "total_entradas": total,
        "perfil": resumen + "\n" + perfil
    })

if __name__ == "__main__":
    app.run(debug=True)
