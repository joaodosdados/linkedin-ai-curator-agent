import feedparser


def fetch_rss_articles(rss_url: str, limit: int = 5):
    feed = feedparser.parse(rss_url)

    articles = []

    for entry in feed.entries[:limit]:
        articles.append(
            {
                'title': entry.get('title'),
                'link': entry.get('link'),
                'summary': entry.get('summary', ''),
            }
        )

    return articles
