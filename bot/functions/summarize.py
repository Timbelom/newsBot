import openai

def summarize_text_from_file(prompt):
    tokenfile = "tokens/openaikey.txt"
    with open(tokenfile, "r") as file:
        for line in file:
            api_key = line.rstrip('\n')
    openai.api_key = api_key
    
    with open("temp/text.txt","r") as file:
        content = file.read()
    prompt_message = prompt + content
    max_tokens = 400  # Adjust the number of tokens as needed for the desired summary length
    response = openai.Completion.create(
        engine="text-davinci-002",  
        prompt=prompt_message,
        max_tokens=max_tokens
    )
    summary = response.choices[0].text
    return summary


