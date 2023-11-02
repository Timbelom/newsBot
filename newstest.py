import requests

url = 'https://www.forbes.com/sites/iainmartin/2023/10/28/saudi-oil-billions-draw-wall-street-to-davos-in-desert-as-israel-hamas-war-rages/'
response = requests.get(url)

print(response.status_code)  # Check the response status code
# print(response.text)  # Print the content to verify it's being retrieved
