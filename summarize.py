"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"
import openai

# Set your OpenAI API key here
api_key = 'YOUR_API_KEY'
openai.api_key = api_key

def summarize_text_from_file(file_path):
    with open(file_path, 'r') as file:
        text = file.read()

    # Set the parameters for the API call
    prompt = f"Summarize the following text: {text}"
    max_tokens = 100  # Adjust the number of tokens as needed for the desired summary length

    # Make an API call to generate the summary
    response = openai.Completion.create(
        engine="text-davinci-002",  # You can choose a different engine depending on your subscription
        prompt=prompt,
        max_tokens=max_tokens
    )

    summary = response.choices[0].text
    return summary

# Example usage
file_path = 'your_text_file.txt'  # Replace with the path to your text file
summary = summarize_text_from_file(file_path)
print(summary)

