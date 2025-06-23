def actualizar_perfil(entradas):
    if not entradas:
        return "Sin suficientes datos para generar un perfil."

    positivos = sum(1 for _, e in entradas if e == "POSITIVO")
    negativos = sum(1 for _, e in entradas if e == "NEGATIVO")
    neutrales = len(entradas) - positivos - negativos

    if positivos > negativos:
        return "Tu perfil emocional es mayormente optimista. Sueles encontrar luz incluso en los días difíciles."
    elif negativos > positivos:
        return "Tu perfil emocional actual muestra tendencia a la introspección y momentos de bajón. Es importante cuidar tu bienestar emocional."
    else:
        return "Tu perfil emocional es equilibrado, con momentos tanto positivos como desafiantes."

def obtener_perfil(entradas):
    return {
        "total_entradas": len(entradas),
        "perfil": actualizar_perfil(entradas)
    }
