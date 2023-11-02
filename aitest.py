import openai

api_key = 'YOUR_API_KEY'  # Replace with your actual API key
prompt = "Once upon a time,"

openai.api_key = api_key

response = openai.Completion.create(
    engine="text-davinci-002",
    prompt=prompt,
    max_tokens=50  # You can adjust this to control the length of the generated text
)

print(response.choices[0].text)
