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

Durante o desenvolvimento, o ChromaDB foi mantido de forma persistente no Google Drive para preservar a base vetorial entre sessões do Google Colab.

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
git clone https://github.com/ABCAdriana/agente-lgpd.git
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

O projeto foi submetido a testes estruturais e a um teste real da
aplicação através do Gradio.

### Teste real com Gemini

Foram realizadas três perguntas no Gradio e as respostas foram
geradas pelo Gemini utilizando o contexto recuperado pelo RAG.

Resultados:

- **O que é dado pessoal segundo a LGPD?** → ✅ resposta correta
- **O que é dado pessoal sensível?** → ✅ resposta correta
- **Quem é o controlador?** → ✅ resposta correta

Esse teste confirmou o fluxo completo:

```text
Pergunta do usuário
    ↓
Gradio
    ↓
Agente
    ↓
Busca no ChromaDB
    ↓
Contexto da LGPD
    ↓
Prompt
    ↓
Gemini
    ↓
Resposta
```

Também foram validados durante o desenvolvimento:

- ChromaDB;
- Embeddings;
- Busca semântica;
- Recuperação de contexto;
- Montagem do prompt;
- Integração do agente com o Gemini;
- Interface Gradio.

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

## 📌 Status do projeto

O funcionamento principal do agente foi concluído e validado.

Concluído:

- Processamento da LGPD;
- Geração dos embeddings;
- ChromaDB persistente;
- Recuperação de contexto;
- RAG;
- Prompt;
- Integração com Gemini;
- Interface Gradio;
- Teste real com três perguntas;
- Versionamento no GitHub.

Próxima etapa de entrega:

- Deploy na Oracle Cloud Infrastructure (OCI);
- Teste final da aplicação após o deploy.

## 👩‍💻 Projeto

Agente de Inteligência Artificial baseado no conteúdo da
Lei Geral de Proteção de Dados Pessoais.