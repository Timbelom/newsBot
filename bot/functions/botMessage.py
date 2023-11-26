import telebot
import json
import time
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
        summary1 = summarise.summarize_text_from_file("Write a one paragraph newsbrief summarizing this text: ") # Replace with your actual summarization logic
        summary2 = summarise.summarize_text_from_file("Write 5-10 esential keywords of this text as hashtags: ") # Replace with your actual summarization logic
        summary = summary1+summary2
        # summary = "tetstst"

        message_text = "**{}**\n---\n{}\n---\n{}\n---\nLink: {}".format(title, description, summary, link)
        bot.send_message(message.chat.id, message_text)

        time.sleep(1)  # Pause for 5 seconds
                
# Start the bot
print("\nBot Initialized")
bot.polling()
