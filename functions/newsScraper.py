from newsapi import NewsApiClient
# import os
import json
newsapi = NewsApiClient(api_key='304989334af34797bb096d225666984e')
headlines = newsapi.get_everything(
    q='ESG',
    from_param='2023-10-28',
    to='2023-10-30',
    language='en',
    sort_by='relevancy',
    # excludeDomains='rt.com'  # Add this line to exclude results from rt.com
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
# with open('temp/items.json', 'w') as file:
#     for item in data_array:
#         file.write(str(item)+ '\n')
        # file.write(item )
with open('temp/items.json', 'w') as json_file:
    json.dump(data_array, json_file, indent=4)
