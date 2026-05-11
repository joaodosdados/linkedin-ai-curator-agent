import os
from dotenv import load_dotenv
from openai import OpenAI


load_dotenv()


SYSTEM_PROMPT = '''
Você é um especialista em criação de conteúdo para LinkedIn.

Seu objetivo é transformar notícias técnicas de IA em posts humanos, naturais, estratégicos e profissionais.

O tom deve parecer um Data Scientist Senior falando sobre tendências reais de IA aplicada.
'''


def get_client():
    api_key = os.getenv('OPENAI_API_KEY')

    if not api_key:
        raise ValueError('OPENAI_API_KEY not found. Create a .env file based on .env.example.')

    return OpenAI(api_key=api_key)


def generate_linkedin_post(topic: str, summary: str):
    prompt = f'''
    Tema: {topic}

    Resumo:
    {summary}

    Gere um post para LinkedIn em português.

    Estrutura:
    - Hook forte
    - Explicação prática
    - Insight pessoal
    - Encerramento curto

    Regras:
    - Não use emojis excessivos.
    - Não pareça um texto genérico de IA.
    - Traga uma opinião prática sobre IA aplicada, dados ou tecnologia em produção.
    '''

    client = get_client()

    response = client.chat.completions.create(
        model=os.getenv('LLM_MODEL', 'gpt-4o-mini'),
        messages=[
            {'role': 'system', 'content': SYSTEM_PROMPT},
            {'role': 'user', 'content': prompt},
        ],
    )

    return response.choices[0].message.content
