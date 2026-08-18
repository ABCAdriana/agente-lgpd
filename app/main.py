import gradio as gr

from .agent import AgenteLGPD


# ============================================================
# AGENTE
# ============================================================

agente = AgenteLGPD()


# ============================================================
# FUNÇÃO DO CHAT
# ============================================================

def responder(mensagem, historico):

    if not mensagem:
        return historico

    try:

        resultado = agente.responder(mensagem, usar_gemini=True)

    except Exception as erro:

        resultado = (
            "⚠️ Não foi possível processar a pergunta no momento.\n\n"
            f"Detalhes: {erro}"
        )

    historico = historico or []

    historico.append({
        "role": "user",
        "content": mensagem
    })

    historico.append({
        "role": "assistant",
        "content": resultado
    })

    return historico


# ============================================================
# INTERFACE
# ============================================================

with gr.Blocks(
    title="Agente LGPD"
) as interface:

    gr.Markdown(
        """
        # 🤖 Agente LGPD

        ### Assistente inteligente baseado na Lei Geral de Proteção de Dados

        Faça perguntas sobre o conteúdo da LGPD.
        """
    )

    chatbot = gr.Chatbot(
        label="Conversa"
    )

    mensagem = gr.Textbox(
        label="Digite sua pergunta",
        placeholder="Ex.: O que é dado pessoal segundo a LGPD?",
        lines=2
    )

    botao = gr.Button("Enviar")

    botao.click(
        responder,
        inputs=[mensagem, chatbot],
        outputs=[chatbot]
    )

    mensagem.submit(
        responder,
        inputs=[mensagem, chatbot],
        outputs=[chatbot]
    )


# ============================================================
# SERVIDOR
# ============================================================

if __name__ == "__main__":

    interface.launch(
        share=True,
        debug=False
    )
