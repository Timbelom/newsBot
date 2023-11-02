import telebot
import json
import time
import requests
from bs4 import BeautifulSoup
import scrapeNews as scrapeNews
import summarize as summarise
import extractor as extractor
# urlsFile = "urlstuff/urls.txt"  
# urls=[]
# with open(urlsFile, "r") as file:
#     for line in file:
#         line = line.rstrip('\n')
#         urls.append(line)
json_file_path = "temp/items.json"
with open(json_file_path, 'r') as json_file:
    articles = json.load(json_file)
        
tokenfile = "token/botToken1.txt"
with open(tokenfile, "r") as file:
    for line in file:
        bot_token = line.rstrip('\n')

# Initialize the Telegram Bot
# bot_token = '6345625037:AAHwIy_QZnLuJaQ0g1dj0j6X1CK-EMC7XJk'
bot = telebot.TeleBot(bot_token)

# Define a command handler for '/start'
@bot.message_handler(commands=['start'])
def send_welcome(message):
    bot.reply_to(message, "Welcome to the Finance News Bot! Use /getnews to get the latest finance news.")

# @bot.message_handler(commands=['getnews'])
# def send_finance_news(message):
#     for i in urls:
#         finance_news = scrapeNews.scrape_finance_news(i)
#         if len(finance_news)>0:

#             for article in finance_news:
#                 title = article['title']
#                 description = article['description']

#                 # Check if the link exists and add it to the message if available
#                 link = article.get('link', 'Link not available')
#                 summary = summarise.summarize_text_from_file()
#                 message_text = f"**{title}**\n{description}\{summary}\nLink: {link}"  
#                 bot.send_message(message.chat.id, message_text)
@bot.message_handler(commands=['getnews'])
def send_finance_news(message):
    for article in articles:
        title = article['title']
        description = article['description']
        link = article['url']
    

        # You mentioned a "summary" function, so call it here if available
        extractor.extract(link)
        summary = summarise.summarize_text_from_file() # Replace with your actual summarization logic

        message_text = f"**{title}**\n{description}\n{summary}\nLink: {link}"
        bot.send_message(message.chat.id, message_text)

        time.sleep(5)  # Pause for 5 seconds
                
# Start the bot
print("\nBot Initialized")
bot.polling()
