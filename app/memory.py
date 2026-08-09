
# ==========================================================
# MEMÓRIA DO AGENTE LGPD
# ==========================================================

class MemoriaAgente:
    """
    Armazena o histórico de perguntas e respostas
    durante a execução da aplicação.
    """

    def __init__(self):
        self.conversas = []


    def adicionar(self, pergunta, resposta):

        self.conversas.append({
            "pergunta": pergunta,
            "resposta": resposta
        })


    def obter_historico(self):

        return self.conversas


    def limpar(self):

        self.conversas = []


    def quantidade(self):

        return len(self.conversas)
