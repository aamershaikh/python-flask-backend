import json
import openai

# Replace with your OpenAI API key
openai.api_key = 'YOUR_OPENAI_API_KEY'

# Load JSON data from a file or a string
json_data = '''
{
    "Type": "Sum",
    "Version": "1.0",
    "PromptDetails": [
        {
            "PromptsSequence": "001",
            "PromptsDescription": "abc",
            "PromptText":"abc"
        },
        {
            "PromptsSequence": "002",
            "PromptsDescription": "def",
            "PromptText":"def"
        },
        {
            "PromptsSequence": "003",
            "PromptsDescription": "pqr",
            "PromptText":"pqr"
        }
    ]
}
'''

data = json.loads(json_data)

# Extract Type
prompt_type = data["Type"]
print(f"Prompt Type: {prompt_type}")

# Function to call OpenAI API
def call_openai_api(prompt_text):
    response = openai.Completion.create(
        engine="text-davinci-003",
        prompt=prompt_text,
        max_tokens=50
    )
    return response.choices[0].text.strip()

# Extract PromptText and call OpenAI API sequentially
for prompt_detail in data["PromptDetails"]:
    prompt_text = prompt_detail["PromptText"]
    print(f"Calling OpenAI API for Prompt: {prompt_text}")
    #response_text = call_openai_api(prompt_text)
    response_text = call_openai_api(prompt_text)
    print(f"Response: {response_text}")

    if prompt_sequence == "001":
            cursor.execute('''
            INSERT INTO prompts (PromptsSequence, Column1)
            VALUES (?, ?)
            ON CONFLICT(PromptsSequence) DO UPDATE SET Column1=excluded.Column1
            ''', (prompt_sequence, response_text))