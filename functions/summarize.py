# "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"
import openai
# Set your OpenAI API key here
api_key = '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'
openai.api_key = api_key
with open("text.txt","r") as file:
    content = file.read()
# print(content)
def summarize_text_from_file():

    # Set the parameters for the API call
    prompt = f"Summarize the following text in form of a news brief: {content}"
    max_tokens = 300  # Adjust the number of tokens as needed for the desired summary length

    # Make an API call to generate the summary
    response = openai.Completion.create(
        engine="text-davinci-002",  # You can choose a different engine depending on your subscription
        prompt=prompt,
        max_tokens=max_tokens
    )

    summary = response.choices[0].text
    return summary

# # Example usage
# file_path = 'text.txt'  # Replace with the path to your text file
summary = summarize_text_from_file()
print(summary)

