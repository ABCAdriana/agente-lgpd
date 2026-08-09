
from sentence_transformers import SentenceTransformer

from .config import EMBEDDING_MODEL


# ==========================================================
# MODELO DE EMBEDDINGS
# ==========================================================

def carregar_modelo_embeddings():
    """
    Carrega o mesmo modelo utilizado para criar
    os embeddings da base LGPD.
    """

    modelo = SentenceTransformer(EMBEDDING_MODEL)

    return modelo
