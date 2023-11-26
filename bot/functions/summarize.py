import openai
import json
import extractor as extractor

def summarize_text_from_file(prompt):
    tokenfile = "tokens/openaikey2.txt"
    with open(tokenfile, "r") as file:
        for line in file:
            api_key = line.rstrip('\n')
    openai.api_key = api_key
    
    with open("temp/text.txt","r") as file:
        content = file.read()
    prompt_message = content + prompt 
    max_tokens = 400  # Adjust the number of tokens as needed for the desired summary length
    response = openai.Completion.create(
        engine="text-davinci-002",  
        prompt=prompt_message,
        max_tokens=max_tokens
    )
    summary = response.choices[0].text
    return summary


def populateResponses():
    for i in range(5):
        responses.append(summarize_text_from_file("Write a one paragraph newsbrief summarizing this text: "))
    # with open('temp/responces.json', 'w') as json_file:
    #     json.dump(responses, json_file, indent=4)

def bestResponse(prompt):
    tokenfile = "tokens/openaikey.txt"
    with open(tokenfile, "r") as file:
        for line in file:
            api_key = line.rstrip('\n')
    openai.api_key = api_key

    prompt_message = str(responses) + prompt 
    max_tokens = 600  # Adjust the number of tokens as needed for the desired summary length
    response = openai.Completion.create(
        engine="text-davinci-002",  
        prompt=prompt_message,
        max_tokens=max_tokens
    )
    summary = response.choices[0].text
    return summary

json_file_path = "temp/items.json"
with open(json_file_path, 'r') as json_file:
    articles = json.load(json_file)
for article in articles:
    print(article['url'])
    extractor.extract(article['url'])
    # with open("temp/text.txt","r") as file:
    #     content = file.read()
    # print(content)
    responses = []
    populateResponses()
    
    article['response'] = bestResponse("Output the most cohesive and understandable of these newsbriefs. ONLY THE NEWSBRIEF. Please remove unnecessary new lines including those before the text.")
        
with open(json_file_path, 'w') as json_file:
    json.dump(articles, json_file, indent=4)
