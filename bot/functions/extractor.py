import requests
from bs4 import BeautifulSoup
import openai

def count_openai_tokens(text):
        response = openai.Completion.create(
            engine="text-davinci-003",
            prompt=text,
            max_tokens=1,
        )
        return response['usage']['total_tokens']
# URL of the webpage to scrape
def extract(url):
    tokenfile = "tokens/openaikey.txt"
    with open(tokenfile, "r") as file:
        for line in file:
            api_key = line.rstrip('\n')
    openai.api_key = api_key
    # Send an HTTP GET request to the URL
    response = requests.get(url)

    # Check if the request was successful
    if response.status_code == 200:
        # Parse the HTML content of the page
        soup = BeautifulSoup(response.text, 'html.parser')

        # Find all the paragraphs in the page
        paragraphs = soup.find_all('p')

        # Create a file and save the paragraphs
        with open('temp/text.txt', 'w', encoding='utf-8') as file:
            token_count = 0
            for paragraph in paragraphs:
                text = paragraph.get_text()
                token_count += count_openai_tokens(text)
                if token_count <= 3000:
                    file.write(text + '\n')
                else:
                    break

        file.close()

        print("Paragraphs extracted and saved to text.txt")
    else:
        print("Failed to retrieve the webpage.")

