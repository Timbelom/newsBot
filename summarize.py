"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"
import openai

# Your OpenAI API key
api_key = "YOUR_API_KEY"

# Text you want to summarize
text_to_summarize = """
Put your extracted text here.
This is the text you want to summarize.
"""

# Define the parameters for the GPT-3 API request
response = openai.Completion.create(
    engine="davinci",
    prompt=f"Summarize the following text:\n{text_to_summarize}\n\nSummary:",
    max_tokens=50,  # Adjust this as needed for your desired summary length
    api_key=api_key
)

# Extract the generated summary
summary = response.choices[0].text.strip()

# Print or save the summary
print("Generated Summary:", summary)

# You can save the summary to a file if needed
with open('summary.txt', 'w', encoding='utf-8') as file:
    file.write(summary)
