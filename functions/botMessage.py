import telebot
import scrapeNews as scrapeNews

urlsFile = "urlstuff/urls.txt"  
urls=[]
with open(urlsFile, "r") as file:
    for line in file:
        line = line.rstrip('\n')
        urls.append(line)
        
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

@bot.message_handler(commands=['getnews'])
def send_finance_news(message):
    for i in urls:
        finance_news = scrapeNews.scrape_finance_news(i)
        if len(finance_news)>0:

            for article in finance_news:
                title = article['title']
                description = article['description']

                # Check if the link exists and add it to the message if available
                link = article.get('link', 'Link not available')

                message_text = f"**{title}**\n{description}\nLink: {link}"  
                bot.send_message(message.chat.id, message_text)
                
        else:
            # error_text = f"Failed to scrape finance news from the provided URL\n"+i
            # bot.send_message(message.chat.id,error_text, disable_web_page_preview=True)
            print(f"Failed to scrape finance news from the provided URL\n"+i)

# Start the bot
print("\nBot Initialized")
bot.polling()
