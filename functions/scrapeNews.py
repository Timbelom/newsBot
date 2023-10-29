import requests
from bs4 import BeautifulSoup
from requests.exceptions import RequestException
def scrape_finance_news(url, timeout=10):
    try:
        response = requests.get(url, timeout=timeout)
        response.raise_for_status()  # Raise an exception for HTTP errors (e.g., 404, 500)

        soup = BeautifulSoup(response.text, 'html.parser')

        news = []
        for article in soup.find_all('article'):
            title_element = article.find('h2')
            description_element = article.find('p')

            if title_element and description_element:
                title = title_element.get_text()
                description = description_element.get_text()

                news.append({'title': title, 'description': description, 'link': url})
        
        return news

    except requests.exceptions.Timeout:
        print(f"Timeout error: The request to {url} timed out.")
    except requests.exceptions.RequestException as e:
        print(f"Request error: An error occurred while fetching {url}. Error: {e}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

    return [url]