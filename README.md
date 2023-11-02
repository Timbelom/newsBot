# newsBot
run.py will update the urls file and run the telegram bot @NewsSource_bot  
newstest.py is a test script to manually verify a given URL  

The FindLatest scripts are tailored scripts to scrape each respective news source  
The scripts in urlStuff are used to add new urls or clear them  
The urls file holds all urls, before adding one manually you could check if it can be scraped via newstest.py  

scrapeNews.py ectracts the needed text from the pages
botMessage.py handles sending the messages
It will not post about bad urls, but they still might break something

token and botToken# hold the needed tokens for the bot



```shell
# Your CMD code here
pip install telebot
pip install bs4
pip install requests
pip install newsapi
pip install openai



