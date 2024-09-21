"""Python script that scrapes the titles and URLs of the
latest articles from a news website (CNN etc). Use
BeautifulSoup and requests for this task."""
import requests
from bs4 import BeautifulSoup

def scrape_latest_news():
    """
    Function to scrape the latest news titles and URLs from CNN
    :return: Object of the list which contains titles and urls of all the latest news
    """
    url = 'https://edition.cnn.com'
    response = requests.get(url)

    if response.status_code != 200:
        print(f"Failed to retrieve webpage. Status code: {response.status_code}")
        return None

    soup = BeautifulSoup(response.content, 'html.parser')
    articles = soup.select('div:nth-child(1) > a:nth-child(2)')

    news_data = []
    for article in articles:
        relative_url = article['href']
        full_url = url + relative_url

        title_element = article.select_one('div > div > span.container__headline-text')
        if title_element:
            title = title_element.get_text(strip=True)
            news_data.append({'title': title, 'url': full_url})

    return news_data

if __name__ == '__main__':
    scrape_latest_news()
    news = scrape_latest_news()
    if news:
        for idx, article in enumerate(news, start=1):
            print(f"{idx}. {article['title']}")
            print(f"   URL: {article['url']}\n")
    else:
        print("error occurred")
