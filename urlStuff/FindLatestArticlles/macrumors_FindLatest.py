import requests
from bs4 import BeautifulSoup
import os

def is_file_empty(file_path):
    return os.path.getsize(file_path) == 0

def FindLatest():
    url = "https://www.macrumors.com"
    urlsFile = "urlStuff/urls.txt" 

    response = requests.get(url)

    if response.status_code == 200:
    
        soup = BeautifulSoup(response.text, 'html.parser')

        # Find the link holder
        latest_article = soup.find('h2', class_='heading--1cooZo6n heading--h4--3n5gZUlc heading--white--2vAPsAl1 heading--noMargin--mnRHPAnD')

        if latest_article:
            # Find the link within theelement
            latest_article_link = latest_article.find('a')

            if latest_article_link:
                # Get the URL of the latest article
                article_url = latest_article_link['href']
                print("URL of the latest article:", article_url, "added to", urlsFile)
                with open(urlsFile, "a") as file:
                    if is_file_empty(urlsFile):
                        file.write(article_url)
                    else:
                        file.write("\n"+article_url)
            else:
                print("No link found in the latest article.")
        else:
            print("No latest article found on the page.")
    else:
        print("Failed to retrieve the page. Status code:", response.status_code)
