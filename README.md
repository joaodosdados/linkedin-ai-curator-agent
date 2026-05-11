# LinkedIn AI Curator Agent

Agente simples para curar notícias de IA, selecionar temas relevantes e gerar rascunhos de posts para LinkedIn.

## Objetivo

Ajudar a manter frequência de publicação no LinkedIn sem perder a voz autoral.

O projeto começa como um MVP com aprovação humana:

1. Coleta notícias de fontes confiáveis de IA.
2. Resume os principais pontos.
3. Ranqueia os temas por relevância.
4. Sugere ângulos de postagem.
5. Gera rascunhos de posts para LinkedIn.
6. Você revisa e publica manualmente.

## Fontes iniciais

- The Batch - DeepLearning.AI
- TLDR AI
- Ben's Bites

As fontes ficam configuradas em `config/sources.yaml`.

## Estrutura

```text
linkedin-ai-curator-agent/
├── app.py
├── requirements.txt
├── .env.example
├── config/
│   └── sources.yaml
├── data/
│   └── .gitkeep
├── prompts/
│   ├── curator_prompt.md
│   └── linkedin_post_prompt.md
└── src/
    ├── main.py
    ├── agents/
    │   ├── curator_agent.py
    │   └── linkedin_writer_agent.py
    ├── collectors/
    │   └── rss_reader.py
    └── utils/
        └── storage.py
```

## Como rodar localmente

```bash
python -m venv .venv
source .venv/bin/activate  # Linux/Mac
# .venv\Scripts\activate   # Windows
pip install -r requirements.txt
cp .env.example .env
```

Depois edite o `.env` com sua chave de API.

Rodar pipeline no terminal:

```bash
python -m src.main
```

Rodar interface:

```bash
streamlit run app.py
```

## Variáveis de ambiente

```env
OPENAI_API_KEY=your_api_key_here
LLM_MODEL=gpt-4o-mini
MAX_ARTICLES_PER_SOURCE=5
```

## Roadmap

- [x] Estrutura inicial do projeto
- [x] Coletor RSS simples
- [x] Curadoria com LLM
- [x] Geração de posts
- [x] Interface Streamlit básica
- [ ] Histórico de posts publicados
- [ ] Score baseado em performance real do LinkedIn
- [ ] Integração com GitHub Trending
- [ ] Agenda editorial semanal
- [ ] Export para Notion/Markdown

## Filosofia

O agente não deve postar automaticamente no começo.

Ele deve automatizar a pesquisa e o primeiro rascunho, mas manter revisão humana para preservar autenticidade, opinião e posicionamento profissional.
