import telebot
import requests
from bs4 import BeautifulSoup
from requests.exceptions import RequestException

urlsFile = "urlstuff/urls.txt"  
urls=[]
with open(urlsFile, "r") as file:
    for line in file:
        # Remove newline character from the end of each line
        line = line.rstrip('\n')
        urls.append(line)

# Initialize the Telegram Bot
bot_token = 'MYTOKEN'
bot = telebot.TeleBot(bot_token)

# Define a function to scrape finance news
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

# Define a command handler for '/start'
@bot.message_handler(commands=['start'])
def send_welcome(message):
    bot.reply_to(message, "Welcome to the Finance News Bot! Use /getnews to get the latest finance news.")

@bot.message_handler(commands=['getnews'])
def send_finance_news(message):
    for i in urls:
        finance_news = scrape_finance_news(i)
        if len(finance_news)>0:

            for article in finance_news:
                title = article['title']
                description = article['description']

                # Check if the link exists and add it to the message if available
                link = article.get('link', 'Link not available')

                message_text = f"**{title}**\n{description}\nLink: {link}"  # Display the link as plain text
                bot.send_message(message.chat.id, message_text)
                
        else:
            # error_text = f"Failed to scrape finance news from the provided URL\n"+i
            # bot.send_message(message.chat.id,error_text, disable_web_page_preview=True)
            print(f"Failed to scrape finance news from the provided URL\n"+i)

# Start the bot
bot.polling()
