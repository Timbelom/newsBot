from newsapi import NewsApiClient
newsapi = NewsApiClient(api_key='304989334af34797bb096d225666984e')
# news_sources = newsapi.get_sources()
# for source in news_sources['sources']:
#     print(source['name'])
headlines = newsapi.get_everything(
    q='ESG',
    from_param='2023-10-28',
    to='2023-10-30',
    language='en',
    sort_by='relevancy'
)
for article in headlines['articles']:
    # print(article)
    print('Title : ',article['title'],"\n")
    print('Description : ',article['description'],"\n")
    print("Url : ", article["url"],"\n")
    content = article["content"]
    # print("content : ", article["content"])
    print(content)
    break
