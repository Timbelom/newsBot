# newsBot
[run.py](run.py) will update the urls file and run the telegram bot @NewsSource_bot  
[newstest.py](newstest.py) is a test script to manually verify a given URL  

The [FindLatest] scripts are tailored scripts to scrape each respective news source  
The scripts in [urlStuff](urlStuff) are used to add new urls or clear them  
The [urls](urlStuff/urls.txt) file holds all urls, before adding one manually you could check if it can be scraped via newstest.py  

[scrapeNews.py](functions/scrapeNews.py) extracts the needed text from the pages
[botMessage.py](functions/botMessage.py) handles sending the messages
It will not post about bad urls, but they still might break something

[token](token) holds the needed tokens for the bot


##### These are the needed libraries 
```shell
pip install telebot
pip install bs4
pip install requests
pip install newsapi
pip install openai