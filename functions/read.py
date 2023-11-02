import ast
import unicodedata
import re

def clean_text(text):
    # Remove undefined or non-Unicode characters
    cleaned_text = ''.join(c for c in text if unicodedata.category(c)[0] != 'C')

    # Replace non-standard characters with their closest Unicode equivalents or remove them
    cleaned_text = re.sub('[“”]', '"', cleaned_text)
    cleaned_text = re.sub('[’‘]', "'", cleaned_text)

    return cleaned_text

def print_content_from_file(file_path):
    try:
        with open(file_path, 'r', encoding='utf-8') as file:
            content = file.read()
            content = clean_text(content)
            content = ast.literal_eval(content)
            for item in content:
                print(f"Title: {item['title']}")
                print(f"Description: {item['description']}")
                print(f"URL: {item['url']}")
                print()
    except FileNotFoundError:
        print(f"File '{file_path}' not found.")
    except (SyntaxError, ValueError) as e:
        print(f"Error parsing Python literals: {e}")

# Provide the file path
file_path = 'temp/text.txt'

# Call the function to read and print content from the file
print_content_from_file(file_path)
