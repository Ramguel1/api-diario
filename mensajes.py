def generar_respuesta(emocion, texto):
    if emocion == "POSITIVO":
        return (
            "¡Qué alegría leer eso! Estás en una buena etapa emocional.",
            "Sigue cultivando estos momentos, dedica tiempo a lo que amas."
        )
    elif emocion == "NEGATIVO":
        return (
            "Parece que estás pasando por un momento difícil.",
            "Es normal sentirse así a veces. Intenta hablar con alguien o salir a caminar, no estás solo/a."
        )
    else:
        return (
            "Tu estado emocional parece equilibrado.",
            "Reflexiona sobre tus pensamientos y permítete sentir con libertad. Todo pasa."
        )
