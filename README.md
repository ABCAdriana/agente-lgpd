# 🤖 Agente LGPD

Agente de Inteligência Artificial especializado em perguntas sobre a 
**Lei Geral de Proteção de Dados Pessoais (LGPD — Lei nº 13.709/2018)**.

O projeto utiliza arquitetura **RAG (Retrieval-Augmented Generation)**, 
permitindo que o modelo Gemini gere respostas baseadas no conteúdo oficial 
da legislação armazenada em uma base vetorial.

---

# 🎯 Objetivo

O objetivo do projeto é desenvolver um agente inteligente capaz de responder 
perguntas relacionadas à LGPD utilizando um documento PDF como fonte de conhecimento.

O agente realiza:

- Leitura e processamento do PDF da LGPD;
- Divisão do documento em trechos (chunks);
- Criação de embeddings;
- Armazenamento em banco vetorial ChromaDB;
- Recuperação dos trechos relevantes;
- Construção de contexto;
- Geração de respostas utilizando Gemini;
- Interface conversacional utilizando Gradio.

---

# 🏗️ Arquitetura


```text
PDF LGPD
↓
Leitura e processamento
↓
Divisão em chunks
↓
Embeddings
↓
ChromaDB
↓
Busca semântica
↓
Contexto relevante
↓
Prompt
↓
Gemini
↓
Resposta ao usuário
↓
Gradio
```

---

# 🧠 Funcionamento do RAG

Quando o usuário realiza uma pergunta:

1. A pergunta é recebida pelo agente;
2. O sistema transforma a pergunta em embedding;
3. O ChromaDB realiza uma busca semântica;
4. Os trechos mais relevantes da LGPD são recuperados;
5. O contexto é enviado ao Gemini;
6. O modelo gera a resposta baseada na legislação.

---

# 📚 Base de conhecimento

Documento utilizado:

**Lei nº 13.709/2018 — Lei Geral de Proteção de Dados Pessoais (LGPD)**

Características:

- Documento em formato PDF;
- 72 chunks gerados;
- Embeddings utilizando:
  `sentence-transformers/all-MiniLM-L6-v2`
- Dimensão dos embeddings: 384;
- Banco vetorial:
  `ChromaDB`
- Coleção:
  `lgpd_conhecimento`

O ChromaDB possui persistência em armazenamento local.

---

# 🛠️ Tecnologias utilizadas

| Tecnologia | Utilização |
|---|---|
| Python | Linguagem principal |
| Google Colab | Ambiente de desenvolvimento |
| Gemini API | Modelo de inteligência artificial generativa |
| LangChain | Orquestração do fluxo RAG |
| PyPDF | Leitura do documento PDF |
| Sentence Transformers | Geração dos embeddings |
| ChromaDB | Banco vetorial |
| Gradio | Interface do agente |
| Docker | Empacotamento |
| GitHub | Versionamento |
| Oracle Cloud OCI | Ambiente de deploy |

---

# 📁 Estrutura do projeto

```text
agente-lgpd/
│
├── app/
│   ├── main.py
│   ├── agent.py
│   ├── rag.py
│   ├── embeddings.py
│   ├── memory.py
│   └── config.py
│
├── data/
│ └── Lei13709_Lgpd.pdf
├── vectorstore/
├── screenshots/
├── notebooks/
│
├── requirements.txt
├── .gitignore
├── Dockerfile
└── README.md
```

# ⚙️ Instalação

Clone o repositório:

```bash
git clone SEU_REPOSITORIO_AQUI
cd agente-lgpd
```

Instale as dependências:

```bash
pip install -r requirements.txt
```

# 🔐 Configuração da API Gemini

A chave da API não deve ser armazenada no código-fonte.

Configure a variável de ambiente:

```bash
export GOOGLE_API_KEY="SUA_CHAVE_AQUI"
```

No Google Colab, a chave pode ser carregada utilizando os recursos
de segurança disponíveis no ambiente.

Nunca publique a chave no GitHub.

# ▶️ Execução

Após configurar as dependências e a variável da API:

```bash
python app/main.py
```

💬 Exemplos de perguntas e respostas
Pergunta:

1-O que é dado pessoal segundo a LGPD?

Resposta gerada:

Informação relacionada a pessoa natural identificada ou identificável.

Pergunta:

2-O que é dado pessoal sensível?

O agente consulta a base da LGPD e apresenta a definição conforme o Art. 5º da Lei nº 13.709/2018.

Pergunta:

3-Quem é considerado titular dos dados?

O agente recupera o conceito de titular presente na legislação.

# 🧪 Validação

Foram realizados testes validando:

Leitura do PDF;
Processamento do documento;
Criação dos chunks;
Geração dos embeddings;
Persistência do ChromaDB;
Recuperação de contexto;
Integração com Gemini;
Interface Gradio.

Teste funcional realizado:

Pergunta:
O que é dado pessoal segundo a LGPD?

Resposta:
Informação relacionada a pessoa natural identificada ou identificável.

# 💬 Histórico

O projeto possui uma camada de memória para armazenar perguntas,
respostas e histórico da conversa.

Arquivo responsável:

```text
app/memory.py
```

# 🛡️ Segurança

Nenhuma informação sensível é armazenada no código-fonte.

O projeto utiliza:

- Variáveis de ambiente;
- Proteção da API Key;
- Arquio.gitignore;
- Separação das configurações;

# 🐳 Docker

O projeto possui um Dockerfile para empacotamento da aplicação.

Construção:

```bash
docker build -t agente-lgpd .
```

Execução:

```bash
docker run -p 7860:7860 agente-lgpd
```

# ☁️ Deploy OCI

O objetivo final é disponibilizar a aplicação na Oracle Cloud
Infrastructure (OCI).

A entrega deverá conter evidências da aplicação funcionando na nuvem.

# ⚠️ Observação sobre o Gemini

Durante o desenvolvimento, os testes de geração foram limitados
para preservar a quota disponível da API.

A recuperação do contexto e a preparação do RAG foram validadas
localmente antes do teste final com o Gemini.

# 👩‍💻 Projeto

Agente de Inteligência Artificial baseado no conteúdo da
Lei Geral de Proteção de Dados Pessoais (LGPD) utilizando arquitetura RAG.
