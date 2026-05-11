import os
import yaml
from dotenv import load_dotenv
from src.collectors.rss_reader import fetch_rss_articles
from src.utils.storage import save_json


load_dotenv()


def load_sources(config_path: str = 'config/sources.yaml'):
    with open(config_path, 'r', encoding='utf-8') as f:
        config = yaml.safe_load(f)
    return config['sources']


def collect_articles():
    max_articles = int(os.getenv('MAX_ARTICLES_PER_SOURCE', '5'))
    sources = load_sources()
    all_articles = []

    for source in sources:
        articles = fetch_rss_articles(source['rss'], limit=max_articles)
        for article in articles:
            article['source'] = source['name']
        all_articles.extend(articles)

    return all_articles


def main():
    articles = collect_articles()
    save_json('data/raw_articles.json', articles)

    print(f'{len(articles)} articles collected and saved to data/raw_articles.json')

    for idx, article in enumerate(articles, start=1):
        print(f"\n[{idx}] {article['title']}")
        print(article['link'])


if __name__ == '__main__':
    main()
