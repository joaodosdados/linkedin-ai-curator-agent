from urllib.parse import urljoin

import feedparser
import requests
from bs4 import BeautifulSoup


HEADERS = {
    'User-Agent': 'Mozilla/5.0 (compatible; LinkedInAICurator/1.0)'
}


def fetch_html_articles(page_url: str, limit: int = 5):
    """Fallback collector for sources that expose articles in HTML instead of RSS."""
    response = requests.get(page_url, headers=HEADERS, timeout=20)
    response.raise_for_status()

    soup = BeautifulSoup(response.text, 'html.parser')
    articles = []
    seen_links = set()

    for tag in soup.find_all(['a', 'h2', 'h3']):
        link_tag = tag if tag.name == 'a' else tag.find('a')
        if not link_tag:
            continue

        title = link_tag.get_text(' ', strip=True)
        href = link_tag.get('href')

        if not title or not href:
            continue

        absolute_link = urljoin(page_url, href)

        if absolute_link in seen_links:
            continue

        if len(title) < 20:
            continue

        articles.append(
            {
                'title': title,
                'link': absolute_link,
                'summary': '',
            }
        )
        seen_links.add(absolute_link)

        if len(articles) >= limit:
            break

    print(f'[INFO] HTML fallback collected {len(articles)} articles from {page_url}')
    return articles


def fetch_rss_articles(rss_url: str, limit: int = 5):
    print(f'[DEBUG] URL: {rss_url}')

    feed = feedparser.parse(rss_url, request_headers=HEADERS)

    status = getattr(feed, 'status', 'unknown')
    print(f'[DEBUG] Feed status: {status}')
    print(f'[DEBUG] Feed entries: {len(feed.entries)}')

    if getattr(feed, 'bozo', False):
        print(f'[WARNING] Feed parsing issue: {rss_url}')

    if not feed.entries:
        print(f'[WARNING] No RSS articles found for: {rss_url}')
        print('[INFO] Trying HTML fallback...')
        try:
            return fetch_html_articles(rss_url, limit=limit)
        except Exception as exc:
            print(f'[ERROR] HTML fallback failed for {rss_url}: {exc}')
            return []

    articles = []

    for entry in feed.entries[:limit]:
        articles.append(
            {
                'title': entry.get('title', 'No title'),
                'link': entry.get('link', ''),
                'summary': entry.get('summary', ''),
            }
        )

    print(f'[INFO] Collected {len(articles)} RSS articles from {rss_url}')

    return articles
