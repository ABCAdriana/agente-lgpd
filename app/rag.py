# ==========================================
# AGENTE LGPD - RAG
# ==========================================

import re


# ==========================================
# BUSCA VETORIAL NORMAL
# ==========================================

def buscar_contexto(pergunta, quantidade_resultados=10):
    """
    Busca os trechos mais relevantes da LGPD
    usando o ChromaDB.
    """

    pergunta_embedding = embeddings_model.encode(
        pergunta,
        convert_to_numpy=True
    ).tolist()

    resultados = collection.query(
        query_embeddings=[pergunta_embedding],
        n_results=quantidade_resultados
    )

    documentos = resultados.get("documents", [[]])[0]

    return documentos


# ==========================================
# DEFINIÇÕES EXATAS DO ART. 5º
# ==========================================

DEFINICOES_ART5 = {

    "dado pessoal": (
        "I - dado pessoal: informação relacionada a pessoa natural "
        "identificada ou identificável;"
    ),

    "dado pessoal sensível": (
        "II - dado pessoal sensível: dado pessoal sobre origem racial "
        "ou étnica, convicção religiosa, opinião política, filiação a "
        "sindicato ou a organização de caráter religioso, filosófico "
        "ou político, dado referente à saúde ou à vida sexual, dado "
        "genético ou biométrico, quando vinculado a uma pessoa natural;"
    ),

    "controlador": (
        "VI - controlador: pessoa natural ou jurídica, de direito "
        "público ou privado, a quem competem as decisões referentes "
        "ao tratamento de dados pessoais;"
    ),

    "operador": (
        "VII - operador: pessoa natural ou jurídica, de direito "
        "público ou privado, que realiza o tratamento de dados "
        "pessoais em nome do controlador;"
    ),

    "encarregado": (
        "VIII - encarregado: pessoa indicada pelo controlador e "
        "operador para atuar como canal de comunicação entre os "
        "titulares dos dados e a Autoridade Nacional de Proteção "
        "de Dados (ANPD);"
    ),

    "agentes de tratamento": (
        "IX - agentes de tratamento: o controlador e o operador;"
    ),

    "tratamento": (
        "X - tratamento: toda operação realizada com dados pessoais"
    ),
}


# ==========================================
# IDENTIFICAÇÃO DA DEFINIÇÃO
# ==========================================

def identificar_definicao_art5(pergunta):
    """
    Identifica perguntas que pedem definições do Art. 5º.
    """

    texto = pergunta.lower().strip()

    # Dado pessoal sensível precisa vir antes de dado pessoal
    if (
        "dado pessoal sensível" in texto
        or "dado sensível" in texto
    ):
        return "dado pessoal sensível"

    if "dado pessoal" in texto:
        return "dado pessoal"

    if "controlador" in texto:
        return "controlador"

    if "operador" in texto:
        return "operador"

    if "encarregado" in texto:
        return "encarregado"

    if "agentes de tratamento" in texto:
        return "agentes de tratamento"

    if re.search(r"\btratamento\b", texto):
        return "tratamento"

    return None


# ==========================================
# BUSCAR DEFINIÇÃO DO ART. 5º
# ==========================================

def buscar_definicao_art5(pergunta, inicio=0):
    """
    Retorna a definição exata do Art. 5º quando
    a pergunta solicitar um conceito definido na LGPD.
    """

    conceito = identificar_definicao_art5(pergunta)

    if conceito is None:
        return None

    return DEFINICOES_ART5.get(conceito)


# ==========================================
# MONTAR CONTEXTO
# ==========================================

def montar_contexto(pergunta, quantidade_resultados=10):
    """
    Monta o contexto que será enviado ao Gemini.

    Para definições do Art. 5º, utiliza a definição
    exata da LGPD.

    Para outras perguntas, utiliza a busca vetorial.
    """

    # ------------------------------------------
    # 1. Tentar definição exata do Art. 5º
    # ------------------------------------------

    definicao = buscar_definicao_art5(pergunta)

    if definicao:
        return definicao

    # ------------------------------------------
    # 2. Busca vetorial para outras perguntas
    # ------------------------------------------

    documentos = buscar_contexto(
        pergunta,
        quantidade_resultados
    )

    if not documentos:
        return ""

    # ------------------------------------------
    # 3. Limpeza dos resultados
    # ------------------------------------------

    documentos_limpos = []

    for documento in documentos:

        if not documento:
            continue

        documento = documento.strip()

        if documento and documento not in documentos_limpos:
            documentos_limpos.append(documento)

    # ------------------------------------------
    # 4. Montar contexto
    # ------------------------------------------

    return "\n\n".join(documentos_limpos)