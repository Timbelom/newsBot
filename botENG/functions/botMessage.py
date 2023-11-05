import telebot
import json
import time
import requests
from bs4 import BeautifulSoup
import summarize as summarise
import extractor as extractor

json_file_path = "temp/items.json"
with open(json_file_path, 'r') as json_file:
    articles = json.load(json_file)
        
tokenfile = "tokens/botToken1.txt"
with open(tokenfile, "r") as file:
    for line in file:
        bot_token = line.rstrip('\n')


bot = telebot.TeleBot(bot_token)

# Define a command handler for '/start'
@bot.message_handler(commands=['start'])
def send_welcome(message):
    bot.reply_to(message, "Welcome to the Finance News Bot! Use /getnews to get the latest finance news.")

@bot.message_handler(commands=['getnews'])
def send_finance_news(message):
    for article in articles:
        title = article['title']
        description = article['description']
        link = article['url']
    

        # You mentioned a "summary" function, so call it here if available
        extractor.extract(link)
        summary = summarise.summarize_text_from_file() # Replace with your actual summarization logic
        
        # summary = "tetstst"

        message_text = f"**{title}**\n{description}\n{summary}\nLink: {link}"
        bot.send_message(message.chat.id, message_text)

        time.sleep(5)  # Pause for 5 seconds
                
# Start the bot
print("\nBot Initialized")
bot.polling()
