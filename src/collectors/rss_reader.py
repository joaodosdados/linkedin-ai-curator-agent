import feedparser


HEADERS = {
    'User-Agent': 'Mozilla/5.0 (compatible; LinkedInAICurator/1.0)'
}


def fetch_rss_articles(rss_url: str, limit: int = 5):
    feed = feedparser.parse(rss_url, request_headers=HEADERS)

    if getattr(feed, 'bozo', False):
        print(f'[WARNING] Feed parsing issue: {rss_url}')

    if not feed.entries:
        print(f'[WARNING] No articles found for: {rss_url}')
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

    print(f'[INFO] Collected {len(articles)} articles from {rss_url}')

    return articles
