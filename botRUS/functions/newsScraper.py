from newsapi import NewsApiClient
import json
from datetime import date, timedelta

end_date = date.today()  # Today's date
start_date = end_date - timedelta(days=7)  # One week ago

with open('tokens/keywordsRUS.txt', 'r', encoding='utf-8') as file:
    keywords = [line.strip() for line in file]

tokenfile = "tokens/newsToken.txt"
with open(tokenfile, "r") as file:
    for line in file:
        token = line.rstrip('\n')

        
newsapi = NewsApiClient(api_key=token)
headlines = newsapi.get_everything(
    q=' OR '.join(keywords) ,
    from_param=start_date.strftime('%Y-%m-%d'),
    to=end_date.strftime('%Y-%m-%d'),
    language='ru',
    sort_by='relevancy',
)

data_array = []
for article in headlines['articles']:
    if 'rt.com' not in article['url']:
        title = article['title']
        description = article['description']
        url = article['url']

        # Append the data to the data_array
        data_array.append({'title': title, 'description': description, 'url': url})
        if len(data_array)>4:
            break

# Print the data_array
for item in data_array:
    print('Title:', item['title'])
    print('Description:', item['description'])
    print('URL:', item['url'])
    print()

with open('temp/items.json', 'w') as json_file:
    json.dump(data_array, json_file, indent=4)
