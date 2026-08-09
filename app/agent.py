
from langchain_google_genai import ChatGoogleGenerativeAI

from .config import GOOGLE_API_KEY, GEMINI_MODEL
from .rag import montar_contexto
from .memory import MemoriaAgente


# ==========================================================
# AGENTE LGPD
# ==========================================================

class AgenteLGPD:

    def __init__(self):

        self.memoria = MemoriaAgente()

        self.llm = None

        # O Gemini só será configurado quando houver
        # uma chave disponível.
        if GOOGLE_API_KEY:

            self.llm = ChatGoogleGenerativeAI(
                model=GEMINI_MODEL,
                google_api_key=GOOGLE_API_KEY,
                temperature=0
            )


    # ======================================================
    # CRIAR PROMPT
    # ======================================================

    def criar_prompt(self, pergunta, contexto):

        prompt = f"""
Você é um assistente especializado na Lei Geral de
Proteção de Dados Pessoais (LGPD - Lei nº 13.709/2018).

Responda à pergunta utilizando somente as informações
presentes no contexto fornecido.

Se a informação não estiver presente no contexto,
informe que não foi possível localizar a resposta
na base de conhecimento da LGPD.

Não invente artigos, números ou informações.

Contexto da LGPD:
{contexto}

Pergunta:
{pergunta}

Resposta:
"""

        return prompt


    # ======================================================
    # RESPONDER
    # ======================================================

    def responder(self, pergunta, usar_gemini=False):

        if not pergunta or not pergunta.strip():

            return "⚠️ Digite uma pergunta sobre a LGPD."


        # Buscar contexto
        contexto = montar_contexto(pergunta)


        if not contexto:

            resposta = (
                "⚠️ Não foi encontrado contexto relevante "
                "na base de conhecimento da LGPD."
            )

            self.memoria.adicionar(
                pergunta,
                resposta
            )

            return resposta


        # Criar prompt
        prompt = self.criar_prompt(
            pergunta,
            contexto
        )


        # ==================================================
        # MODO OFFLINE
        # ==================================================

        if not usar_gemini:

            resposta = (
                "Teste estrutural concluído. "
                "O agente recuperou corretamente o contexto "
                "da LGPD e preparou o prompt.\n\n"
                f"Tamanho do contexto utilizado: "
                f"{len(contexto)} caracteres."
            )

            self.memoria.adicionar(
                pergunta,
                resposta
            )

            return resposta


        # ==================================================
        # MODO GEMINI
        # ==================================================

        if self.llm is None:

            resposta = (
                "⚠️ A API do Gemini não está configurada "
                "ou a chave não está disponível."
            )

            self.memoria.adicionar(
                pergunta,
                resposta
            )

            return resposta


        try:

            resultado = self.llm.invoke(prompt)

            resposta = resultado.content

        except Exception:

            resposta = (
                "⚠️ Não foi possível gerar a resposta "
                "com o Gemini no momento. "
                "O contexto da LGPD foi recuperado "
                "corretamente."
            )


        # Registrar conversa
        self.memoria.adicionar(
            pergunta,
            resposta
        )


        return resposta
