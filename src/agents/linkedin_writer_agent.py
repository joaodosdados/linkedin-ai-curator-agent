from openai import OpenAI
import os


client = OpenAI(api_key=os.getenv('OPENAI_API_KEY'))


SYSTEM_PROMPT = '''
Você é um especialista em criação de conteúdo para LinkedIn.

Seu objetivo é transformar notícias técnicas de IA em posts humanos, naturais, estratégicos e profissionais.

O tom deve parecer um Data Scientist Senior falando sobre tendências reais de IA aplicada.
'''


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

    Não use emojis excessivos.
    '''

    response = client.chat.completions.create(
        model=os.getenv('LLM_MODEL', 'gpt-4o-mini'),
        messages=[
            {'role': 'system', 'content': SYSTEM_PROMPT},
            {'role': 'user', 'content': prompt},
        ],
    )

    return response.choices[0].message.content
