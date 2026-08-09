
import chromadb

from .config import CHROMA_DIR, COLLECTION_NAME
from .embeddings import carregar_modelo_embeddings


# ==========================================================
# CARREGAR MODELO DE EMBEDDINGS
# ==========================================================

embeddings_model = carregar_modelo_embeddings()


# ==========================================================
# CARREGAR CHROMADB
# ==========================================================

def carregar_collection():

    cliente = chromadb.PersistentClient(
        path=str(CHROMA_DIR)
    )

    collection = cliente.get_or_create_collection(
        name=COLLECTION_NAME
    )

    return collection


collection = carregar_collection()


# ==========================================================
# BUSCAR CONTEXTO
# ==========================================================

def buscar_contexto(pergunta, quantidade_resultados=3):
    """
    Busca os trechos mais relevantes da LGPD
    para uma determinada pergunta.
    """

    pergunta_embedding = embeddings_model.encode(
        pergunta,
        convert_to_numpy=True
    ).tolist()

    resultados = collection.query(
        query_embeddings=[pergunta_embedding],
        n_results=quantidade_resultados
    )

    return resultados


# ==========================================================
# MONTAR CONTEXTO
# ==========================================================

def montar_contexto(pergunta, quantidade_resultados=3):

    resultados = buscar_contexto(
        pergunta,
        quantidade_resultados
    )

    documentos = resultados.get("documents", [[]])

    if not documentos or not documentos[0]:
        return ""

    contexto = "\n\n".join(documentos[0])

    return contexto
