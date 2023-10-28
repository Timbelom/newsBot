import requests

url = 'https://www.cnet.com/tech/computing/best-e-ink-tablets/'
response = requests.get(url)

print(response.status_code)  # Check the response status code
print(response.text)  # Print the content to verify it's being retrieved
