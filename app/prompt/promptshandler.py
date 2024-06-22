import json
import openai

# Replace with your OpenAI API key
openai.api_key = 'OPENAI_API_KEY'

# Load JSON data from a local file
with open('prompts.json', 'r') as file:
    data = json.load(file)

# Extract Type and PromptDetails
prompt_type = data["Type"]
prompt_details = data["PromptDetails"]

print(f"Prompt Type: {prompt_type}")

# Function to call OpenAI API
def call_openai_api(prompt_text):
    response = openai.Completion.create(
        engine="text-davinci-003",
        prompt=prompt_text,
        max_tokens=50
    )
    return response.choices[0].text.strip()

# Function to call OpenAI API
def call_openai_api(prompt_text):
    response = openai.Completion.create(
        engine="text-davinci-003",
        prompt=prompt_text,
        max_tokens=50
    )
    return response.choices[0].text.strip()

# Process each PromptDetail
for prompt_detail in prompt_details:
    prompt_sequence = prompt_detail["PromptsSequence"]
    prompt_text = prompt_detail["PromptText"]

    print(f"Calling OpenAI API for PromptSequence {prompt_sequence}: {prompt_text}")
    response_text = call_openai_api(prompt_text)
    print(f"Response: {response_text}")

    # Update database based on PromptSequence
    if prompt_sequence == "001":
        account_entry = session.query(Account).first()
        if account_entry:
            account_entry.summarizationavailable = response_text
        else:
            account_entry = Account(summarizationavailable=response_text)
            session.add(account_entry)
    elif prompt_sequence == "002":
        account_entry = session.query(Account).first()
        if account_entry:
            account_entry.accountsummary = response_text
        else:
            account_entry = Account(accountsummary=response_text)
            session.add(account_entry)
    elif prompt_sequence == "003":
        account_entry = session.query(Account).first()
        if account_entry:
            account_entry.accountdetails = response_text
        else:
            account_entry = Account(accountdetails=response_text)
            session.add(account_entry)

# Commit changes to the database
session.commit()
session.close()