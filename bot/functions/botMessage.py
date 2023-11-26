import telebot
import json
import time

channelIDFile = "tokens/channelID.txt"
with open(channelIDFile, "r") as file:
    for line in file:
        CHANNEL_ID = line.rstrip('\n')
        
json_file_path = "temp/items.json"
with open(json_file_path, 'r') as json_file:
    articles = json.load(json_file)
        
tokenfile = "tokens/botToken1.txt"
with open(tokenfile, "r") as file:
    for line in file:
        bot_token = line.rstrip('\n')


bot = telebot.TeleBot(bot_token)

# # Define a command handler for '/start'
# @bot.message_handler(commands=['start'])
# def send_welcome(message):
#     bot.reply_to(message, "Welcome to the Finance News Bot! Use /getnews to get the latest finance news.")

# @bot.message_handler(commands=['getnews'])
def send_finance_news():
    print("\nBot Initialized")
    for article in articles:
        message_text = "**{}**\n---\n{}\n---\n{}\n---\nLink: {}".format(article['title'], article['description'], article["response"], article['url'])
        bot.send_message(chat_id=CHANNEL_ID, text=message_text)

        time.sleep(1)  # Pause for 5 seconds
                
# Start the bot
send_finance_news()

# bot.polling()
