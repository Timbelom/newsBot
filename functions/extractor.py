import requests
from bs4 import BeautifulSoup

# URL of the webpage to scrape
url = "https://www.forbes.com/sites/iainmartin/2023/10/28/saudi-oil-billions-draw-wall-street-to-davos-in-desert-as-israel-hamas-war-rages/"

# Send an HTTP GET request to the URL
response = requests.get(url)

# Check if the request was successful
if response.status_code == 200:
    # Parse the HTML content of the page
    soup = BeautifulSoup(response.text, 'html.parser')

    # Find all the paragraphs in the page
    paragraphs = soup.find_all('p')

    # Create a file and save the paragraphs
    with open('text.txt', 'w', encoding='utf-8') as file:
        for paragraph in paragraphs:
            file.write(paragraph.get_text() + '\n')

    print("Paragraphs extracted and saved to text.txt")
else:
    print("Failed to retrieve the webpage.")

