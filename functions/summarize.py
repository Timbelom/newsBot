import openai

def summarize_text_from_file():
    tokenfile = "tokens/openaikey.txt"
    with open(tokenfile, "r") as file:
        for line in file:
            api_key = line.rstrip('\n')
    openai.api_key = api_key
    
    with open("temp/text.txt","r") as file:
        content = file.read()
    # Set the parameters for the API call
    prompt = f"Summarize the following text in form of a news brief, make it 2 to 3 paragraphs of the most important information: {content}"
    max_tokens = 300  # Adjust the number of tokens as needed for the desired summary length

    # Make an API call to generate the summary
    response = openai.Completion.create(
        engine="text-davinci-002",  # You can choose a different engine depending on your subscription
        prompt=prompt,
        max_tokens=max_tokens
    )
    summary = response.choices[0].text
    return summary


