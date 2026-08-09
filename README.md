# 🤖 Agente LGPD

Agente de Inteligência Artificial especializado em perguntas sobre a
Lei Geral de Proteção de Dados Pessoais (LGPD — Lei nº 13.709/2018).

## 🎯 Objetivo

O projeto utiliza arquitetura RAG (Retrieval-Augmented Generation)
para recuperar informações relevantes da LGPD antes da geração da resposta.

O agente é capaz de:

- Ler e processar o documento da LGPD em PDF;
- Dividir o documento em trechos;
- Criar embeddings;
- Armazenar os embeddings no ChromaDB;
- Recuperar os trechos mais relevantes;
- Utilizar o Gemini para gerar respostas baseadas no contexto;
- Manter histórico das conversas;
- Disponibilizar uma interface utilizando Gradio.

## 🏗️ Arquitetura

```text
PDF da LGPD
    ↓
Leitura e processamento
    ↓
Divisão em chunks
    ↓
Embeddings
    ↓
ChromaDB
    ↓
Retriever
    ↓
Contexto relevante
    ↓
Prompt
    ↓
Gemini
    ↓
Resposta ao usuário
```

## 🧠 RAG

Quando o usuário realiza uma pergunta, o sistema:

1. Recebe a pergunta;
2. Realiza uma busca semântica;
3. Recupera os trechos mais relevantes da LGPD;
4. Monta o contexto;
5. Cria o prompt;
6. Envia o contexto para o Gemini;
7. Retorna a resposta ao usuário.

## 📚 Base de conhecimento

Documento utilizado:

**Lei nº 13.709/2018 — Lei Geral de Proteção de Dados Pessoais (LGPD)**

Características da base:

- 72 chunks;
- Embeddings com dimensão 384;
- Modelo: sentence-transformers/all-MiniLM-L6-v2;
- Coleção ChromaDB: lgpd_conhecimento.

O ChromaDB foi configurado para persistência durante o desenvolvimento.

## 🛠️ Tecnologias utilizadas

| Tecnologia | Utilização |
|---|---|
| Python | Linguagem principal |
| Google Colab | Desenvolvimento |
| Gemini | Inteligência artificial generativa |
| PyPDF | Leitura do PDF |
| LangChain | Orquestração |
| Sentence Transformers | Embeddings |
| ChromaDB | Banco vetorial |
| Gradio | Interface |
| Docker | Empacotamento |
| GitHub | Versionamento |
| Oracle Cloud OCI | Deploy |

## 📁 Estrutura do projeto

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
├── vectorstore/
├── screenshots/
├── notebooks/
│
├── requirements.txt
├── .gitignore
├── Dockerfile
└── README.md
```

## ⚙️ Instalação

Clone o repositório:

```bash
git clone SEU_REPOSITORIO_AQUI
cd agente-lgpd
```

Instale as dependências:

```bash
pip install -r requirements.txt
```

## 🔐 Configuração da API Gemini

A chave da API não deve ser armazenada no código-fonte.

Configure a variável de ambiente:

```bash
export GOOGLE_API_KEY="SUA_CHAVE_AQUI"
```

No Google Colab, a chave pode ser carregada utilizando os recursos
de segurança disponíveis no ambiente.

Nunca publique a chave no GitHub.

## ▶️ Execução

Após configurar as dependências e a variável da API:

```bash
python app/main.py
```

## 💬 Exemplos de perguntas

- O que é dado pessoal segundo a LGPD?
- O que é dado pessoal sensível?
- Quem é considerado titular dos dados?
- O que é tratamento de dados pessoais?
- Quem é o controlador?
- Quem é o operador?
- Quais são os direitos do titular?

## 🧪 Validação

Durante o desenvolvimento, a recuperação do contexto foi validada
sem realizar chamadas adicionais ao Gemini.

Exemplo:

> O que é dado pessoal segundo a LGPD?

O sistema conseguiu recuperar o contexto da base LGPD e preparar
o prompt para o modelo.

Foram validados:

- ChromaDB;
- Embeddings;
- Busca semântica;
- Recuperação de contexto;
- Montagem do prompt.

## 💬 Histórico

O projeto possui uma camada de memória para armazenar perguntas,
respostas e histórico da conversa.

Arquivo responsável:

```text
app/memory.py
```

## 🛡️ Segurança

Informações sensíveis não são armazenadas diretamente no código.

O projeto utiliza:

- Variáveis de ambiente;
- .gitignore;
- Separação das configurações;
- Proteção da chave da API.

## 🐳 Docker

O projeto possui um Dockerfile para empacotamento da aplicação.

Construção:

```bash
docker build -t agente-lgpd .
```

Execução:

```bash
docker run -p 7860:7860 agente-lgpd
```

## ☁️ Deploy OCI

O objetivo final é disponibilizar a aplicação na Oracle Cloud
Infrastructure (OCI).

A entrega deverá conter evidências da aplicação funcionando na nuvem.

## ⚠️ Observação sobre o Gemini

Durante o desenvolvimento, os testes de geração foram limitados
para preservar a quota disponível da API.

A recuperação do contexto e a preparação do RAG foram validadas
localmente antes do teste final com o Gemini.

## 👩‍💻 Projeto

Agente de Inteligência Artificial baseado no conteúdo da
Lei Geral de Proteção de Dados Pessoais.