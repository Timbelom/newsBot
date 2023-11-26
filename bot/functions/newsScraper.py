from newsapi.newsapi_client import NewsApiClient
import json
from datetime import date, timedelta, datetime

end_date = date.today()  # Today's date
start_date = end_date - timedelta(days=7)  # One week ago

# with open('tokens/keywordsENG.txt', 'r', encoding='utf-8') as file:
#     keywords = [line.strip() for line in file]

tokenfile = "tokens/newsToken.txt"
with open(tokenfile, "r") as file:
    for line in file:
        token = line.rstrip('\n')

        
newsapi = NewsApiClient(api_key=token)

def load_filter_params_from_json(json_file_path):
    with open(json_file_path, 'r', encoding='utf-8') as config_file:  # Specify UTF-8 encoding
        config = json.load(config_file)
    return config

def get_news_headlines(filter_params, desired_language):
    # Create a NewsApiClient instance (make sure you have the API key)

    # Find the filter that matches the desired language
    selected_filter = None
    for filter in filter_params['filters']:
        if filter['language'] == desired_language:
            selected_filter = filter
            break

    if selected_filter is None:
        return []  # No filter found for the desired language

    # Extract filter parameters from the selected filter
    keywords = selected_filter['keywords']
    to_date = datetime.now()
    from_date = to_date - timedelta(days=7) 
    sort_by = selected_filter['sort_by']

    # Create the search query by joining the keywords with "OR"
    query = ' OR '.join(keywords)

    # Get headlines with the selected filter parameters
    headlines = newsapi.get_everything(
        q=query,
        from_param=from_date.strftime('%Y-%m-%d'),
        to=to_date.strftime('%Y-%m-%d'),
        language=desired_language,
        sort_by=sort_by,
    )

    return headlines


data_array = []
headlines = get_news_headlines(load_filter_params_from_json("bot/searchFilters.json"),"en")
for article in headlines['articles']:
    if 'rt.com' and 'journals.plos.org' not in article['url']:
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
