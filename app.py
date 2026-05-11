import streamlit as st
from pathlib import Path
from src.utils.storage import load_json
from src.agents.linkedin_writer_agent import generate_linkedin_post


st.set_page_config(page_title='LinkedIn AI Curator', layout='wide')

st.title('LinkedIn AI Curator Agent')
st.caption('Editorial dashboard for AI content curation')


articles_path = Path('data/raw_articles.json')

if not articles_path.exists():
    st.warning('No articles found. Run: python -m src.main')
    st.stop()


articles = load_json('data/raw_articles.json')

selected_article = st.selectbox(
    'Choose an article',
    articles,
    format_func=lambda x: f"[{x['source']}] {x['title']}"
)


st.subheader(selected_article['title'])
st.write(selected_article['summary'])
st.link_button('Open article', selected_article['link'])


if st.button('Generate LinkedIn Post'):
    with st.spinner('Generating post...'):
        generated_post = generate_linkedin_post(
            selected_article['title'],
            selected_article['summary']
        )

    st.session_state['generated_post'] = generated_post


if 'generated_post' in st.session_state:
    st.subheader('Editable LinkedIn Draft')

    edited_text = st.text_area(
        'Edit your post',
        value=st.session_state['generated_post'],
        height=400
    )

    st.download_button(
        label='Download draft',
        data=edited_text,
        file_name='linkedin_post.txt',
        mime='text/plain'
    )
