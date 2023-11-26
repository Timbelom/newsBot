# newsBot
[run.py](run.py) will update the urls file and run the telegram bot @NewsSource_bot \
[newstest.py](newstest.py) is a test script to manually verify a given URL  

[newsScraper.py](functions/newsScraper.py) finds and stores article info into [items.json](temp/items.json) \
[extractor.py](functions/extractor.py) extracts the needed text from the pages \
[summarize.py](functions/summarize.py) uses davinci Ai processing to summarize each article \
[botMessage.py](functions/botMessage.py) handles sending the messages \
It will not post about bad urls, but they still might break something

[token](token) holds the needed tokens for the bot


##### These are the needed libraries 
```shell
pip install telebot
pip install bs4
pip install requests
pip install newsapi-python
pip install openai
```
<img src="imgs/newsbot flow.jpg"/>


